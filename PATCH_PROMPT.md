# Small Patch Prompt

Use this prompt when asking an AI coding assistant to work on one GOWN task.

```text
You are helping with a small open-source Python proof of concept.

Do not expand the project vision.
Do not add coin, market, fundraising, or broad capability claims.
Do not rewrite the architecture.
Do not add unnecessary dependencies.
Make the smallest useful patch.

Repo:
https://github.com/sherlockholmesyes/open-weights-network

Task:
<paste one task card from TASKS.md>

Current constraints:
- Python >=3.10
- standard-library first
- existing demo must keep working
- tests should use unittest
- do not log raw prompts or raw outputs

Output:
1. brief summary
2. files changed
3. test command
4. unified diff or PR link
5. risks or assumptions
```
