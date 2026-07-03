# Contributing

GOWN is early infrastructure. The most useful contributions are small,
test-backed patches.

## Before opening a PR

- Pick one task from `TASKS.md`, or open an issue for a similarly small task.
- Keep the existing demo working.
- Prefer the Python standard library.
- Add or update tests when behavior changes.
- Do not log raw prompts or raw outputs.
- Do not add broad marketing claims.
- Do not add a coin, market, or fundraising layer.
- Do not submit broad rewrites as a first contribution.

## Local checks

```bash
python -m unittest discover -s tests
python -m gown_poc.demo
```

## PR format

Include:

- task id
- summary
- files changed
- test command and result
- any risk or follow-up

## AI-assisted patches

AI-assisted patches are welcome, but review the diff before submitting. You are
responsible for the final patch.
