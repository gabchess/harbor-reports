from harbor.report import pipeline_total, weekly_report

ROWS = [
    {"deal": "Pier 4 renewal", "stage": "won", "amount": "1200.00", "close_date": "2026-11-16"},
    {"deal": "Dockside upsell", "stage": "open", "amount": "800.00", "close_date": "2026-11-18"},
]


def test_weekly_report_counts_deals_by_stage():
    report = weekly_report(ROWS)
    assert report["deals"] == 2
    assert report["by_stage"] == {"won": 1, "open": 1}
    assert report["total"] == 2000
    assert report["week"] == "Nov 16 to Nov 22"


def test_pipeline_total_rounds_once_after_adding():
    rows = [{"amount": "0.50"}, {"amount": "0.50"}]
    assert pipeline_total(rows) == 1.0
