import csv

from harbor.dates import parse_day, week_label


def read_export(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def pipeline_total(rows):
    return round(sum(float(row["amount"]) for row in rows), 2)


def weekly_report(rows):
    stages = {}
    for row in rows:
        stages[row["stage"]] = stages.get(row["stage"], 0) + 1
    first_day = min(parse_day(row["close_date"]) for row in rows)
    return {
        "week": week_label(first_day),
        "deals": len(rows),
        "total": pipeline_total(rows),
        "by_stage": stages,
    }
