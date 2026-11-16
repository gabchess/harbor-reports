import csv

from harbor.export import write_csv
from harbor.report import weekly_report
from tests.test_report import ROWS


def test_write_csv_has_a_row_per_stage_and_a_total(tmp_path):
    path = tmp_path / "weekly.csv"
    write_csv(weekly_report(ROWS), path)
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.reader(handle))
    assert rows == [["stage", "deals"], ["open", "1"], ["won", "1"], ["total", "2000"]]
