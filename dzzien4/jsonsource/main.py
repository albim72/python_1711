from dataclasses import dataclass
from typing import List
import json


@dataclass
class RunRecord:
    date: str
    distance_km: float
    duration_min: float


class RunLog:
    def __init__(self):
        self.runs: List[RunRecord] = []

    def add_run(self, run:RunRecord):
        self.runs.append(run)

    def total_distance(self) -> float:
        return sum(r.distance_km for r in self.runs)

    @staticmethod
    def _paces_min_per_km(run:RunRecord) -> float:
        return run.duration_min / run.distance_km if run.distance_km > 0 else 0

    def load_from_json(self, path:str):
        with open(path, "r",encoding="utf-8") as f:
            data = json.load(f)
        for item in data["runs"]:
            self.add_run(
                RunRecord(
                    date = item["date"],
                    distance_km = item["distance_km"],
                    duration_min= item["duration_min"],))

    def export_json(self,path: str):
        data = {
            "runs": [
                {
                    "date":r.date,
                    "distance_km": r.distance_km,
                    "duration_min": r.duration_min
                }
                for r in self.runs
            ]
        }

        with open(path, "w",encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    log = RunLog()
    log.load_from_json("runs.json")

    #dodajemy nowe biegi
    log.add_run(RunRecord("2023-11-18", 5, 24))
    log.add_run(RunRecord("2023-11-19", 12, 67))
    log.add_run(RunRecord("2023-11-20", 80, 670))

    log.export_json("runs.json")

    print(f"suma kilometrów: {log.total_distance():.2f} km")


if __name__ == '__main__':
    main()

