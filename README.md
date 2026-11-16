# Harbor Reports

Harbor Reports turns a sales team's pipeline export into a weekly report a manager reads in two minutes. It lists the total pipeline, the deals that moved and the deals that slipped.

Harbor Reports is a fictional product. This repo is the sandbox for Launch Factory, which turns merged pull requests and product briefings into launch content. Every person, team and number in it is made up.

## What is here

| Path | What it holds |
| --- | --- |
| `harbor/` | The product stub. `report.py` builds the weekly report from a CSV export. |
| `tests/` | One test of the weekly report. Run it with `python -m pytest`. |
| `marketing/` | The positioning and voice files the agent reads before it writes. |
| `briefings/` | Two product briefings, each with its properties and expected verdict. |
| `examples/` | Six example pull requests, each with its title, body and expected verdict. |
| `docs/` | The placeholder page GitHub Pages serves. |

## How changes reach main

The main branch is protected. Every change reaches it through a pull request, and a direct push is refused.
