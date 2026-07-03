# GOWN Small Task Queue

Pick one task, reply with the task id, and submit one small patch. These tasks
are intentionally narrow so they can be finished from a Reddit thread without a
long planning phase.

## How to claim

```text
Taking GOWN-003. I will keep it stdlib-only and post a PR/diff when done.
```

## Shared rules

- Keep the existing demo working.
- Prefer `unittest` and Python standard library.
- Do not log raw prompts or raw outputs.
- Do not add coin, market, fundraising, or broad capability claims.
- Do not rewrite the architecture.
- One task per PR.

## GOWN-001: Add route trace schema and example

Estimated time: 20-45 minutes.

Goal: define a minimal JSONL trace format for routing decisions.

Files:

```text
schemas/route_trace.schema.json
examples/route_trace.example.jsonl
```

Trace fields:

```text
trace_id
task_hash
router_version
candidate_nodes
chosen_node
model_id
gate_reports
latency_ms
cost_units
privacy_level
created_at
```

Acceptance:

- Example JSONL line matches the schema shape.
- Trace stores a task hash, not raw prompt text.
- Trace stores metadata only, not raw model output.
- No runtime dependency is added.

Suggested reply:

```text
GOWN-001 done: added route trace schema and example JSONL.
Tests: python -m unittest discover -s tests
```

## GOWN-002: Add serialization helpers for protocol objects

Estimated time: 45-90 minutes.

Goal: make existing protocol objects easy to write into traces.

Files:

```text
gown_poc/protocol.py
tests/test_smoke.py or tests/test_serialization.py
```

Add `to_dict` / `from_dict` helpers for:

```text
ModelCard
NodeCard
InferenceTask
InferenceReply
GateReport
```

Acceptance:

- Roundtrip test for `ModelCard`.
- Roundtrip test for `NodeCard`.
- Existing demo output still works.
- No routing behavior change.

## GOWN-003: Make the demo write route_trace.jsonl

Estimated time: 45-90 minutes.

Goal: every demo route writes one minimal trace line.

Files:

```text
gown_poc/trace.py
gown_poc/demo.py
tests/test_trace.py
```

Output path:

```text
runs/demo/route_trace.jsonl
```

Acceptance:

- `python -m gown_poc.demo` still prints the routing report.
- It also writes one JSONL trace line.
- Test confirms the raw prompt text is absent from the trace file.
- `route_trace.jsonl` is ignored by git unless it is under `examples/`.

## GOWN-004: Add backend adapter interface

Estimated time: 45-90 minutes.

Goal: prepare `Router.call` to use real backends without breaking the mock demo.

Files:

```text
gown_poc/backends/base.py
gown_poc/backends/mock.py
gown_poc/protocol.py or gown_poc/demo.py
tests/test_backends.py
```

Define:

```text
BackendAdapter
generate(task, node, model) -> InferenceReply
```

Acceptance:

- Existing demo behavior remains equivalent.
- Tests cover the mock adapter.
- Router no longer hardcodes reply text directly if the extraction stays clean.
- No real HTTP calls yet.

## GOWN-005: Add llama.cpp adapter stub with fake server tests

Estimated time: 60-90 minutes.

Goal: add a minimal HTTP adapter shape for a local llama.cpp-compatible server.

Files:

```text
gown_poc/backends/llamacpp.py
tests/test_llamacpp_adapter.py
```

Rules:

- Do not require a real model in tests.
- Do not require llama.cpp installed for tests.
- Use a fake local HTTP server from the standard library.
- Endpoint must be configurable.
- Convert the response into `InferenceReply`.
- Handle timeout and malformed response.

Acceptance:

- Tests pass with the fake server.
- Adapter is not used by the default demo unless explicitly selected.
- No broad refactor.

## GOWN-006: Add example validation command

Estimated time: 30-60 minutes.

Goal: provide a simple command that checks example cards for required fields.

Files:

```text
gown_poc/validate_examples.py
tests/test_validate_examples.py
Makefile
```

Acceptance:

- `python -m gown_poc.validate_examples` checks existing examples.
- Missing required fields produce a non-zero exit.
- `make test` or a new `make validate` target runs it.
- No external JSON Schema dependency is required.

## GOWN-007: Add router policy config example

Estimated time: 45-75 minutes.

Goal: move basic router thresholds into a small config object and example file.

Files:

```text
gown_poc/protocol.py
examples/router_policy.json
tests/test_router_policy.py
```

Fields:

```text
min_health_score
allowed_privacy_levels
max_latency_ms
max_cost_units
```

Acceptance:

- Defaults preserve current demo behavior.
- Example policy file is documented.
- Test proves a stricter policy can reject a node that the default would accept.

## GOWN-008: Add OpenAI-compatible gateway skeleton

Estimated time: 60-90 minutes.

Goal: add a small HTTP gateway skeleton without making it the default runtime.

Files:

```text
gown_poc/gateway.py
tests/test_gateway.py
```

Endpoints:

```text
GET /health
GET /v1/models
POST /v1/chat/completions
```

Rules:

- Use the standard library HTTP server.
- The chat endpoint may route to the existing mock path.
- Do not log raw request messages.
- Keep this opt-in; the demo should still work without starting a server.

Acceptance:

- Test starts the gateway on a random local port.
- `/health` returns OK.
- `/v1/models` returns known model ids.
- `/v1/chat/completions` returns a response shaped like a simple chat completion.

## GOWN-009: Add node health report object

Estimated time: 30-60 minutes.

Goal: separate node health reporting from routing decisions.

Files:

```text
gown_poc/protocol.py
tests/test_health_report.py
```

Add:

```text
NodeHealthReport
node_id
observed_at
health_score
latency_ms
available_models
errors
```

Acceptance:

- Health report can be serialized.
- Router can keep using the current `NodeCard.health_score`.
- No routing behavior change unless explicitly covered by tests.
