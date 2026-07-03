---
name: Small task
about: Claim or propose a small GOWN task
title: "Task: "
labels: task
assignees: ""
---

## Task id

GOWN-___

## Goal

What should this small patch accomplish?

## Files likely touched

```text

```

## Acceptance

- [ ] Existing demo still works.
- [ ] Tests added or updated if behavior changes.
- [ ] No raw prompt or raw output logging.
- [ ] No broad rewrite.

## Test command

```bash
python -m unittest discover -s tests
python -m gown_poc.demo
```
