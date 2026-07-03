# Contributor Rigor Pack

Credit: inspired by Iwo Szapar's Rigor Pack:
https://www.iwoszapar.com/tools/rigor-pack

This file is an original adaptation for this repository. It does not copy the
source pack's skill bodies.

## Why This Exists

GOWN is a small public proof-of-concept for an open-weight inference mesh.
The best contributions are narrow, test-backed, and easy for a reviewer to
verify from the repository alone.

## Usefulness Check

Useful here:

- it forces a plan before changing files;
- it makes contributors verify the current repository state instead of relying
  on stale docs;
- it keeps pull requests narrow;
- it requires proof from commands, files, or demo output;
- it keeps public docs free of secrets, raw prompts, raw outputs, and private
  material.

Not enough by itself:

- it does not replace tests, demos, or schema checks;
- it does not prove capacity, privacy, or availability without a measured gate;
- it should not be treated as an external authority over this repo's design.

## Contributor Loop

Before editing:

```text
Task:
Files expected:
Non-scope:
Acceptance command:
Risk if wrong:
```

During editing:

```text
Keep the diff small.
Do not change unrelated files.
Do not add raw prompts, raw outputs, secrets, or private notes.
Map every claim to a file, test, or demo result.
```

Before opening a PR:

```text
Run the relevant command.
Paste the exact command and result.
Name one way the patch could still be wrong.
List adjacent issues under "noticed, not changed".
```

## GOWN Local Gates

For ordinary changes:

```bash
python -m unittest discover -s tests
python -m gown_poc.demo
```

Or, if `make` is available:

```bash
make test
make demo
```

## PR Format

```text
Task:
Files changed:
Non-scope:
Proof command:
Proof result:
Adversarial check:
Noticed, not changed:
Source credit, if adapting an external idea:
```

## Review Rules

A PR is easier to merge when:

- it strengthens one routing, registry, privacy, health, or reply contract;
- it adds or updates tests when behavior changes;
- it updates docs only when docs match the runnable demo;
- it avoids broad claims about capacity or reliability without measurement.

A PR should be split when:

- it mixes routing logic, node schemas, docs, and public messaging;
- it changes unrelated task areas;
- it needs more than one acceptance command to explain what it proves.
