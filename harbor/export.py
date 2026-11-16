import csv


def write_csv(report, path):
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["stage", "deals"])
        for stage, deals in sorted(report["by_stage"].items()):
            writer.writerow([stage, deals])
        writer.writerow(["total", report["total"]])
