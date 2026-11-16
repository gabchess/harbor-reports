# Add CSV export

- Branch: `claude/example-csv-export`
- Expected verdict: write
- Tier: launch
- Gates opened: blog, changelog, social, FAQ

## Pull request title

Add CSV export

## Pull request body

Adds a CSV download of the weekly report.

Managers asked for a way to send the weekly report to their director or load it into a spreadsheet. The weekly report can now be saved as a CSV file with one row per stage and a total row at the end.

- New `harbor/export.py` with `write_csv(report, path)`.
- The file has the columns stage and deals, then a total row with the pipeline total.
- One new test checks the rows in the written file.
