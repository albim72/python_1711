"""
CREATE TABLE runs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    run_date DATE NOT NULL,
    distance_km DOUBLE NOT NULL,
    duration_min DOUBLE NOT NULL
);


INSERT INTO runs (run_date, distance_km, duration_min) VALUES
('2025-08-11', 10, 47),
('2025-08-12', 12, 58),
('2025-08-17', 5, 24),
('2025-08-19', 36, 233);

"""

from dataclasses import dataclass
from typing import List
import mysql.connector  # pip install mysql-connector-python


@dataclass
class RunRecord:
    date: str          # np. "2025-08-11"
    distance_km: float
    duration_min: float


class RunLog:
    def __init__(self):
        self.runs: List[RunRecord] = []

    def add_run(self, run: RunRecord):
        self.runs.append(run)

    def total_distance(self) -> float:
        return sum(r.distance_km for r in self.runs)

    @staticmethod
    def _pace_min_per_km(run: RunRecord) -> float:
        return run.duration_min / run.distance_km if run.distance_km > 0 else 0

    def export_txt(self, path: str):
        with open(path, 'w', encoding='utf-8') as f:
            for r in self.runs:
                pace = self._pace_min_per_km(r)
                line = (
                    f"{r.date} | "
                    f"{r.distance_km:.1f}km | "
                    f"{r.duration_min:.1f}min | "
                    f"{pace:.2f}min/km\n"
                )
                f.write(line)
            f.write(f"SUMA: {self.total_distance():.1f}km\n")


def load_runs_from_mysql(
    host: str,
    user: str,
    password: str,
    database: str
) -> List[RunRecord]:
    """Pobiera dane biegów z tabeli runs w MySQL i zwraca listę RunRecord."""
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )
    try:
        cursor = conn.cursor()
        # dopasowane do struktury tabeli: run_date, distance_km, duration_min
        cursor.execute("SELECT run_date, distance_km, duration_min FROM runs")
        records: List[RunRecord] = []
        for run_date, distance_km, duration_min in cursor:
            # run_date jest typu date → zamieniamy na string
            records.append(
                RunRecord(
                    date=str(run_date),
                    distance_km=float(distance_km),
                    duration_min=float(duration_min),
                )
            )
        return records
    finally:
        conn.close()


def main():
    # 1. Wczytujemy dane z MySQL
    runs_from_db = load_runs_from_mysql(
        host="localhost",
        user="twoj_user",
        password="twoje_haslo",
        database="running_db",
    )

    # 2. Budujemy RunLog na podstawie rekordów z bazy
    log = RunLog()
    for r in runs_from_db:
        log.add_run(r)

    # 3. Eksport do pliku tekstowego + podsumowanie
    log.export_txt("runs.txt")
    print(f"Razem: {log.total_distance():.2f} km")


if __name__ == '__main__':
    main()
