# Refactor date helpers

- Branch: `claude/example-date-helpers-refactor`
- Expected verdict: skip
- Tier: none
- Gates opened: none

## Pull request title

Refactor date helpers

## Pull request body

Replaces the hand written date parser in `harbor/dates.py` with `date.fromisoformat`.

No behavior change. The existing test passes unchanged.
