# GOWN Small Task Handoff

This repository is a small open-source PoC for routing local/open-weight model
inference across eligible nodes.

The best contributions right now are small infrastructure patches, not broad
architecture proposals.

## Current scope

Make the existing PoC easier to test, route, trace, and eventually connect to a
real local model backend.

## Non-goals

- no coin, market, or fundraising layer
- no broad capability claims
- no distributed training work in this repo
- no unauthorized data scraping
- no competitor distillation
- no broad architecture rewrite
- no raw prompt or raw output logging in traces

## Start here

Repository:

```text
https://github.com/sherlockholmesyes/open-weights-network
```

Relevant files:

```text
gown_poc/protocol.py
gown_poc/demo.py
schemas/model_card.schema.json
schemas/node_card.schema.json
examples/node_card.json
tests/test_smoke.py
```

## Contribution rules

- One small task per PR.
- Keep the diff under roughly 300 lines when practical.
- Prefer the Python standard library unless a task explicitly allows a dependency.
- Add or update tests.
- Keep the existing demo working.
- Do not rename the project.
- Do not add hype language.
- Do not log raw prompts or raw outputs.
- If using an AI coding assistant, review the patch before submitting.

## Output format

Submit one of:

1. GitHub PR.
2. GitHub issue with a unified diff.
3. Reddit reply with:
   - task id
   - summary
   - files changed
   - test command
   - diff or branch link

## Test command

```bash
python -m unittest discover -s tests
python -m gown_poc.demo
```
