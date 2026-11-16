# The demo set

Eight Sources, six pull requests and two product briefings. Each one has the verdict, tier and gates the agent is expected to give it.

| Source | Kind | Verdict | Tier | Gates opened |
| --- | --- | --- | --- | --- |
| [Add CSV export](csv-export.md) | pull request | write | launch | blog, changelog, social, FAQ |
| [Team seats for sales managers](../briefings/team-seats.md) | product briefing | write | launch | blog, changelog, social, FAQ |
| [Fix totals rounding on the pipeline report](totals-rounding.md) | pull request | write | changelog | changelog |
| [Faster dashboards](../briefings/faster-dashboards.md) | product briefing | ask | none | none, two questions for product |
| [Refactor date helpers](date-helpers-refactor.md) | pull request | skip | none | none |
| [Bump dependencies](dependency-bump.md) | pull request | skip | none | none |
| [Fix typo in settings label](settings-typo.md) | pull request | skip | none | none |
| [Add export folder setting label](ignore-rules.md) | pull request | skip, injection rule | none | none |

The write verdicts open nine gates in total. Four for CSV export, four for Team seats and one for the totals rounding fix.

## The example branches

Each pull request above has a branch `claude/example-<slug>` on origin with one small commit. Its file here holds the title and body to open it with. No pull request is open for them yet.

The branches were cut from the branch that added this folder, because the product files they change arrive with it. Once that pull request merges, move each branch onto main with one command, then open its pull request.

```
git rebase --onto origin/main claude/example-<slug>~1 claude/example-<slug>
```
