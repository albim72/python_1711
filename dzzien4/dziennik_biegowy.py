from dataclasses import dataclass
from typing import List

# list = [5,4,3,7]
# a: List[int] = [5,4,3,7]

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

    def export_txt(self,path:str):
        with open(path,"w",encoding="utf-8") as f:
            for r in self.runs:
                pace = self._paces_min_per_km(r)
                line = f"{r.date} | {r.distance_km} km | {r.duration_min} min | {pace:.1f} min/km\n"
                f.write(line)
            f.write(f"Total distance: {self.total_distance():.1f} km\n")

def main():
    log = RunLog()
    log.add_run(RunRecord("2025-11-01", 10, 47))
    log.add_run(RunRecord("2025-11-06", 12, 59))
    log.add_run(RunRecord("2025-11-07", 5, 27))
    log.add_run(RunRecord("2025-11-09", 36, 233))
    log.add_run(RunRecord("2025-11-12", 21, 117.5))
    log.add_run(RunRecord("2025-11-14", 8, 41))
    log.add_run(RunRecord("2025-11-18", 54, 363.8))

    log.export_txt("dziennik_biegowy.txt")
    print(f"Razem: {log.total_distance():.2f} km")

if __name__ == '__main__':
    main()

