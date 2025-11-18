from __future__ import annotations

from typing import Any, Dict, List, Optional
import random

import networkx as nx


class NarrativeMap:
    """
    Narrative decision-tree map for tabletop or story-driven games.

    The map is represented as a directed tree rooted in the ``"start"`` node.
    Each node holds an event description, while edges represent player choices
    with associated risk and reward values.

    :param themes: List of narrative themes (e.g. redemption, mystery).
    :type themes: list[str]
    :param locations: List of key locations for the narrative.
    :type locations: list[str]
    :param characters: List of main characters.
    :type characters: list[str]
    :param seed: Random seed for deterministic generation. If ``None``,
                 a non-deterministic generator is used.
    :type seed: int | None

    :Example:

        .. code-block:: python

            nm = NarrativeMap(
                themes=["odkupienie", "tajemnica"],
                locations=["opuszczony zamek", "mglista dolina"],
                characters=["Wędrowiec", "Cień"],
            )
            nm.build_tree(depth=2)
            path = ["start", "start_L", "start_LL"]
            summary = nm.get_path_summary(path)
            print(summary["n_steps"])  # 2
    """

    def __init__(
        self,
        themes: List[str],
        locations: List[str],
        characters: List[str],
        seed: Optional[int] = 42,
    ) -> None:
        """
        Initialize a new narrative map.

        :param themes: List of narrative themes (e.g. redemption, mystery).
        :type themes: list[str]
        :param locations: List of key locations for the narrative.
        :type locations: list[str]
        :param characters: List of main characters.
        :type characters: list[str]
        :param seed: Random seed for deterministic generation. If ``None``,
                     a non-deterministic generator is used.
        :type seed: int | None
        """
        self.themes: List[str] = list(themes)
        self.locations: List[str] = list(locations)
        self.characters: List[str] = list(characters)
        self.seed: Optional[int] = seed

        self.graph: nx.DiGraph = nx.DiGraph()

        if seed is not None:
            self._rng = random.Random(seed)
        else:
            self._rng = random.Random()

        self._choice_pairs: List[tuple[str, str]] = [
            ("zaufaj", "zdrada"),
            ("ucieknij", "staw czoła"),
            ("przyjmij znak", "zignoruj ostrzeżenie"),
            ("wejdź głębiej", "wycofaj się"),
            ("poświęć coś", "chroń siebie"),
        ]
        self._choice_index: int = 0

    def build_tree(self, depth: int = 3) -> None:
        """
        Build the narrative decision tree of a given depth.

        The tree is rooted in the node with id ``"start"``. Each non-leaf node
        will have at least two outgoing edges (choices), with contrasting labels
        taken from predefined choice pairs (e.g. ``"zaufaj"`` vs. ``"zdrada"``).
        Edge attributes include ``choice``, ``risk`` and ``reward`` (1–10).

        The method clears any existing graph data before building a new tree.

        :param depth: Maximum depth of the tree, counting edges from the root
                      (e.g. ``3`` produces paths of length 3 from ``"start"``).
        :type depth: int
        :raises ValueError: If ``depth`` is less than 1.

        :Example:

            .. code-block:: python

                nm = NarrativeMap(["odkupienie"], ["zamek"], ["Wędrowiec"])
                nm.build_tree(depth=2)
                print(sorted(nm.graph.nodes()))
        """
        if depth < 1:
            raise ValueError("Tree depth must be at least 1.")

        self.graph.clear()
        self._choice_index = 0

        root_id = "start"
        self.graph.add_node(
            root_id,
            description=self._generate_event_description(root_id),
        )

        self._expand_node(root_id, current_depth=0, max_depth=depth)

    def get_path_summary(self, path: List[str]) -> Dict[str, Any]:
        """
        Compute a summary for a given path from root to leaf.

        The path is a list of node identifiers, starting at ``"start"`` and
        proceeding through consecutive nodes in the tree. The method returns:

        * ``events``: list of event descriptions for the nodes in the path,
        * ``choices``: list of edge labels between consecutive nodes,
        * ``total_risk``: sum of ``risk`` attributes along the path,
        * ``total_reward``: sum of ``reward`` attributes along the path,
        * ``n_steps``: number of transitions along the path.

        :param path: List of node identifiers representing a path
                     from root to leaf (inclusive).
        :type path: list[str]
        :returns: Dictionary with aggregated path information.
        :rtype: dict[str, Any]
        :raises ValueError: If any node in the path does not exist in the graph
                            or if two consecutive nodes are not connected
                            by a directed edge.

        :Example:

            .. code-block:: python

                nm = NarrativeMap(["odkupienie"], ["zamek"], ["Wędrowiec"])
                nm.build_tree(depth=2)
                path = ["start", "start_L", "start_LL"]
                summary = nm.get_path_summary(path)
                print(summary["n_steps"])  # 2
        """
        if not path:
            raise ValueError("Path cannot be empty.")

        for node_id in path:
            if node_id not in self.graph:
                raise ValueError(f"Node '{node_id}' is not present in the graph.")

        events: List[str] = []
        for node_id in path:
            description = self.graph.nodes[node_id].get("description")
            if description is None:
                raise ValueError(f"Node '{node_id}' has no 'description' attribute.")
            events.append(description)

        choices: List[str] = []
        total_risk = 0
        total_reward = 0

        for i in range(len(path) - 1):
            src = path[i]
            dst = path[i + 1]
            if not self.graph.has_edge(src, dst):
                raise ValueError(f"Edge '{src}' -> '{dst}' does not exist in the graph.")

            edge_data = self.graph[src][dst]
            choice_label = edge_data.get("choice")
            risk = edge_data.get("risk")
            reward = edge_data.get("reward")

            if choice_label is None or risk is None or reward is None:
                raise ValueError(
                    f"Edge '{src}' -> '{dst}' is missing required attributes."
                )

            choices.append(str(choice_label))
            total_risk += int(risk)
            total_reward += int(reward)

        n_steps = max(0, len(path) - 1)

        return {
            "events": events,
            "choices": choices,
            "total_risk": total_risk,
            "total_reward": total_reward,
            "n_steps": n_steps,
        }

    def _expand_node(self, node_id: str, current_depth: int, max_depth: int) -> None:
        """
        Recursively expand a node to build the tree.

        This is an internal helper that attaches two children to each
        non-leaf node, assigning contrasting choice labels and random
        risk/reward values.

        Node identifiers follow a readable pattern, e.g.:

        * ``"start"``
        * ``"start_L"``, ``"start_R"``
        * ``"start_LL"``, ``"start_LR"``, ``"start_RL"``, ``"start_RR"``, etc.

        :param node_id: Identifier of the node to expand.
        :type node_id: str
        :param current_depth: Current depth of this node.
        :type current_depth: int
        :param max_depth: Maximum depth allowed for the tree.
        :type max_depth: int
        """
        if current_depth >= max_depth:
            return

        pair = self._choice_pairs[self._choice_index % len(self._choice_pairs)]
        self._choice_index += 1

        directions = ["L", "R"]
        labels = [pair[0], pair[1]]

        for direction, choice_label in zip(directions, labels):
            if node_id == "start":
                child_id = f"{node_id}_{direction}"
            else:
                # Append direction without extra underscore for deeper levels
                child_id = f"{node_id}{direction}"

            if child_id not in self.graph:
                self.graph.add_node(
                    child_id,
                    description=self._generate_event_description(child_id),
                )

            risk_value = self._rng.randint(1, 10)
            reward_value = self._rng.randint(1, 10)

            self.graph.add_edge(
                node_id,
                child_id,
                choice=choice_label,
                risk=risk_value,
                reward=reward_value,
            )

            self._expand_node(
                child_id,
                current_depth=current_depth + 1,
                max_depth=max_depth,
            )

    def _generate_event_description(self, node_id: str) -> str:
        """
        Generate a short narrative description for a given node.

        This method simulates a call to an LLM to obtain a 2–3 sentence
        description. It deterministically combines themes, locations and
        characters using an internal random number generator.

        :param node_id: Identifier of the narrative node.
        :type node_id: str
        :returns: Human-readable description of the event.
        :rtype: str
        """
        # TODO: call GPT here

        theme = self._rng.choice(self.themes) if self.themes else "tajemnicza nuta"
        location = (
            self._rng.choice(self.locations)
            if self.locations
            else "nieokreślone miejsce"
        )
        character = (
            self._rng.choice(self.characters)
            if self.characters
            else "Nieznajomy"
        )

        depth_level = max(0, node_id.count("L") + node_id.count("R"))
        phase_word = {
            0: "początek",
            1: "pierwszy zwrot",
            2: "punkt przełomowy",
            3: "głębokie wejście",
        }.get(depth_level, "ostatnia próba")

        description = (
            f"{character} dociera do {location}, gdzie motyw {theme} zaczyna wybrzmiewać "
            f"z niespodziewaną siłą ({phase_word} opowieści). "
            f"W powietrzu unosi się echo dawnych decyzji, a kolejny krok na ścieżce "
            f"\"{node_id}\" może raz na zawsze odmienić los wszystkich bohaterów."
        )

        return description


if __name__ == "__main__":
    themes = ["odkupienie", "tajemnica"]
    locations = ["opuszczony zamek", "mglista dolina"]
    characters = ["Wędrowiec", "Cień"]

    narrative_map = NarrativeMap(
        themes=themes,
        locations=locations,
        characters=characters,
    )
    narrative_map.build_tree(depth=3)

    # Left-most path: start -> start_L -> start_LL -> start_LLL
    sample_path = ["start", "start_L", "start_LL", "start_LLL"]

    summary = narrative_map.get_path_summary(sample_path)

    print("=== Podsumowanie ścieżki ===")
    print("Ścieżka węzłów:", " -> ".join(sample_path))
    print("\nZdarzenia:")
    for i, event in enumerate(summary["events"], start=1):
        print(f"  [{i}] {event}")

    print("\nWybory:")
    for i, choice in enumerate(summary["choices"], start=1):
        print(f"  Krok {i}: {choice}")

    print("\nŁączne wartości:")
    print(f"  Ryzyko  : {summary['total_risk']}")
    print(f"  Nagroda : {summary['total_reward']}")
    print(f"  Kroki   : {summary['n_steps']}")

    print("\n=== Krawędzie w grafie (choice, risk, reward) ===")
    for src, dst, data in narrative_map.graph.edges(data=True):
        print(
            f"{src} -> {dst}: "
            f"choice={data.get('choice')}, "
            f"risk={data.get('risk')}, "
            f"reward={data.get('reward')}"
        )
