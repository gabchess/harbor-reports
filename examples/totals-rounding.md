# Fix totals rounding on the pipeline report

- Branch: `claude/example-totals-rounding`
- Expected verdict: write
- Tier: changelog
- Gates opened: changelog

## Pull request title

Fix totals rounding on the pipeline report

## Pull request body

The pipeline report rounded each deal to a whole number before adding them up. On a report with many deals under a dollar apart, the total could be off by a few dollars.

The total now adds the exact amounts and rounds once, to two decimals.

- `pipeline_total` in `harbor/report.py` sums first and rounds once.
- A new test covers two deals of 0.50 each, which used to total 0.
