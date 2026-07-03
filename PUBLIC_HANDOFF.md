# GOWN Public Handoff Pack

Repository: https://github.com/sherlockholmesyes/godworks-open-weights-network  
Public framing name: **GOWN - local/open-weight inference router PoC**  
Audience: OSS contributors, local LLM users, backend adapter builders  
Status: **early runnable PoC, not a product**

## 0. One-line public pitch

GOWN is a small Python PoC for routing open-weight inference across local or LAN nodes using machine-readable model cards, node cards, health/privacy gates, and minimal route traces.

Use this pitch publicly:

```text
I'm looking for small boring infrastructure patches for an open-weight inference router: ModelCard, NodeCard, route_trace.jsonl, health gates, and llama.cpp/vLLM adapter work. No token, no fundraising, no broad capability claims, no broad rewrite.
```

## 1. Current scope

The current repo is useful as a routing skeleton. The immediate goal is to make it capable of calling one real local backend and writing one replayable trace per routed task.

Current baseline:

```bash
python -m gown_poc.demo
python -m unittest discover -s tests
make demo
make test
```

Current objects to preserve:

- `ModelCard`: model identity, hash, quantization, context, capabilities, license, VRAM requirement.
- `NodeCard`: endpoint, GPU/VRAM, hosted models, health, trust/privacy modes, latency/cost, signature.
- `InferenceTask`: prompt-bearing request object used by router.
- `GateReport`: accepted/rejected routing decision with reasons.
- `Router`: filters candidates and picks one node/model.

Current limitation:

- `Router.call` still returns a mock reply.
- There is no real backend adapter yet.
- There is no durable route trace writer yet.
- There is no node daemon yet.
- There is no public mesh; keep work local-first.

## 2. Non-goals for public tasks

Do not add any of the following in contributor patches:

- token launch, marketplace, resale, or fundraising language
- hype, revolution, or civilization-scale claims
- distributed training
- remote hidden-state model parallelism
- raw prompt or raw output logging
- broad architecture rewrites
- new dependencies unless the task explicitly allows them
- cryptographic or blockchain claims without implementation
- new branding or culture-war language

Public contributions should look like normal OSS infrastructure work.

## 3. Contributor rules

- One small task per PR or diff.
- Keep diffs under roughly 300 lines when possible.
- Prefer Python stdlib.
- Use `unittest` for tests.
- Keep `python -m gown_poc.demo` working.
- Keep existing public APIs working unless the task says otherwise.
- Add tests for new behavior.
- Do not log raw prompts or outputs in traces.
- Use hashes or commitments for prompt/output-related fields.
- Include test command and result in every handoff.

## 4. Missing bricks

| Brick | Current state | Why it matters | Smallest useful task |
|---|---:|---|---|
| RouteTrace format | missing/proto | Routing needs replayable evidence without prompt leaks. | Add schema + example JSONL. |
| Trace writer | missing | Demo should produce durable routing evidence. | Write one trace line for demo route. |
| Serialization helpers | partial/missing | Cards/reports need stable JSON output. | `to_dict`/`from_dict` tests for cards and reports. |
| Backend adapter interface | missing | Router should not hardcode mock replies. | Add `BackendAdapter` + mock adapter. |
| llama.cpp adapter | missing | First real local backend for GGUF/consumer nodes. | HTTP adapter tested with fake server. |
| vLLM adapter | missing | First high-throughput GPU backend path. | OpenAI-compatible adapter tested with fake server. |
| ModelCard schema | partial | ModelCard should be a runnable contract, not just Python dataclass. | JSON schema + validation command/test. |
| NodeCard schema | partial | Node should expose resource/profile contract. | JSON schema + validation command/test. |
| Node daemon | missing | A node needs stable profile/serve/health commands. | `gown node profile` and `gown node health`. |
| Health probe | missing | Router needs fresh node state. | Probe endpoint and mark stale/unhealthy. |
| Registry persistence | missing | In-memory registry blocks LAN testing. | SQLite registry for nodes/models. |
| Fallback policy | missing | Route should survive node loss. | If chosen node fails, try next accepted node. |
| Reputation score | missing | Repeated failures should affect routing. | Local failure/latency counters only. |
| LAN mesh | missing | Need 23 node test before public networking. | Manual registry + heartbeat + fallback demo. |
| Privacy policy | partial | Public tasks must not leak prompts. | Trace privacy test and documentation. |

## 5. High-priority contributor task queue

### GOWN-001  Public README neutralization

Goal: make the repo readable as boring OSS infrastructure.

Change:

- Add `Status: early runnable PoC, not a product` near the top.
- Add `What this is` and `What this is not` sections.
- Remove profanity/culture-war phrasing from public README text.
- Keep the technical architecture intact.
- Avoid token, broad capability, large-scale, or revolution language.

Acceptance:

- README explains the project in under 60 seconds.
- No code changes.
- Maintainer/moderator would not read it as spam or hype.

Patch prompt:

```text
Make a minimal README-only diff for this repo. Keep the technical content, but make the public framing boring, contributor-friendly, and moderator-safe. Do not add hype/token/fundraising language. Do not rename the project. Output a unified diff.
```

### GOWN-002  Add RouteTrace schema and example

Goal: define a minimal JSONL trace format for routing decisions.

Add:

- `schemas/route_trace.schema.json`
- `examples/route_trace.example.jsonl`

Fields:

- `trace_id`
- `task_hash`
- `router_version`
- `candidate_nodes`
- `chosen_node`
- `model_id`
- `gate_reports`
- `latency_ms`
- `cost_units`
- `privacy_level`
- `created_at`

Rules:

- Do not include raw prompt.
- Do not include raw output.
- Keep schema small and readable.

Acceptance:

- Example JSONL is valid JSON per line.
- Schema documents required fields.
- No runtime dependency required.

Patch prompt:

```text
Add a minimal route_trace.jsonl schema and one example trace line. The trace must record routing decisions without storing raw prompts or outputs. Keep this as a small additive patch. Output files changed, test command, and unified diff.
```

### GOWN-003  Serialization helpers for protocol objects

Goal: make existing dataclasses usable in traces and future APIs.

Files:

- `gown_poc/protocol.py`
- `tests/test_protocol_serialization.py`

Add serialization for:

- `ModelCard`
- `NodeCard`
- `InferenceTask`
- `InferenceReply`
- `GateReport`

Acceptance:

- Round-trip test for `ModelCard`.
- Round-trip test for `NodeCard`.
- Existing demo still works.
- No routing behavior change.

Patch prompt:

```text
Add small to_dict/from_dict helpers for the existing protocol dataclasses and unittest coverage. Preserve behavior. Do not add dependencies. Do not refactor routing. Output a unified diff.
```

### GOWN-004  Make demo write `route_trace.jsonl`

Goal: every demo route writes one minimal trace line.

Add:

- `gown_poc/trace.py`
- output path: `runs/demo/route_trace.jsonl`

Trace should record:

- task hash, not raw prompt
- candidate node ids
- gate reports
- chosen node id
- chosen model id
- latency/cost
- router version

Acceptance:

- `python -m gown_poc.demo` still prints routing report.
- It also writes a JSONL trace line.
- Test confirms prompt text is not present in the trace file.

Patch prompt:

```text
Add a small trace writer and update the demo so it writes one route_trace.jsonl line. Never store the raw prompt or output. Add a unittest that fails if the prompt text appears in the trace. Keep the patch narrow.
```

### GOWN-005  Backend adapter interface with mock default

Goal: separate routing from model execution.

Add:

- `gown_poc/backends/base.py`
- `gown_poc/backends/mock.py`
- tests for mock adapter

Interface:

```python
class BackendAdapter:
    def generate(self, task, node, model):
        ...
```

Acceptance:

- Existing demo output remains equivalent.
- Router can use a backend adapter instead of hardcoding reply text.
- Mock remains the default.
- No real HTTP calls yet.

Patch prompt:

```text
Introduce a minimal backend adapter interface and a mock implementation. Preserve current behavior. Do not add llama.cpp or vLLM yet. Keep tests stdlib-only and use unittest.
```

### GOWN-006  llama.cpp adapter stub with fake server test

Goal: add the first real backend adapter shape without requiring a model in CI.

Add:

- `gown_poc/backends/llamacpp.py`
- tests using a fake local HTTP server

Rules:

- Do not require llama.cpp installed for tests.
- Do not require a real model file.
- Endpoint must be configurable.
- Convert response into `InferenceReply`.
- Handle timeout and invalid response.

Acceptance:

- Tests pass with fake server.
- Adapter is not used by default demo unless explicitly selected.
- No broad refactor.

Patch prompt:

```text
Add a minimal llama.cpp-compatible HTTP adapter tested with a fake stdlib HTTP server. Do not require real llama.cpp, a model file, or external dependencies. Convert the fake server response into InferenceReply. Keep patch small.
```

### GOWN-007  vLLM/OpenAI-compatible adapter stub

Goal: support OpenAI-compatible local servers such as vLLM without making them required.

Add:

- `gown_poc/backends/openai_compatible.py`
- fake HTTP server test

Request target:

- `/v1/chat/completions`

Acceptance:

- Adapter reads endpoint from node/model configuration or constructor.
- Tests use fake server only.
- Bad HTTP status and malformed JSON are handled.
- No dependency on `openai` package.

Patch prompt:

```text
Add an OpenAI-compatible HTTP backend adapter using only the Python stdlib. Test it with a fake local HTTP server. Do not add the openai package. Keep it optional and not used by default.
```

### GOWN-008  JSON schema validation command

Goal: make card files checkable from CLI.

Add:

- `schemas/model_card.schema.json`
- `schemas/node_card.schema.json`
- `gown_poc/card_validation.py`
- tests

Acceptance:

- Valid example cards pass.
- Missing required fields fail.
- CLI exits nonzero on invalid input.
- No new dependency unless justified.

Patch prompt:

```text
Add minimal JSON schemas and a stdlib validation command for ModelCard and NodeCard. Structural validation is enough. Include valid/invalid tests. Do not broaden scope.
```

### GOWN-009  Minimal node daemon CLI

Goal: give nodes stable commands without building a platform.

Add commands:

```bash
gown node profile
gown node health
```

Acceptance:

- `profile` prints a NodeCard-like JSON object.
- `health` prints health JSON with timestamp and status.
- No long-running server required yet.
- Tests call command entry functions directly.

Patch prompt:

```text
Add a minimal node CLI with profile and health commands. Do not implement a full daemon or network registry yet. Output JSON. Keep tests stdlib-only.
```

### GOWN-010  SQLite node registry

Goal: persist local nodes and model cards for LAN testing.

Add:

- `gown_poc/registry_store.py`
- tests with temporary SQLite database

Acceptance:

- Register node.
- List nodes.
- Load node into router-compatible object.
- Reject duplicate node id.
- Use Python stdlib `sqlite3`.

Patch prompt:

```text
Add a tiny SQLite registry store for NodeCard records using stdlib sqlite3. Include tests for insert/list/load/duplicate rejection. Do not change router policy.
```

### GOWN-011  Fallback routing test

Goal: if a selected backend fails, router can try the next accepted node.

Change:

- Add a small fallback method or wrapper.
- Use mock adapters that fail/succeed in tests.

Acceptance:

- First accepted node failure leads to second accepted node attempt.
- Trace/report records the failure reason.
- No retry storm.

Patch prompt:

```text
Add a narrow fallback routing test and implementation using mock backend adapters. If the first accepted node fails, try the next accepted node once. Record the failure in the route report. Keep scope small.
```

### GOWN-012  Privacy guard test for traces

Goal: prevent accidental prompt/output logging.

Add:

- test helper that scans trace files for known prompt/output strings
- docs note in `docs/TRACE_PRIVACY.md`

Acceptance:

- Test fails if raw prompt appears in `route_trace.jsonl`.
- Test fails if raw output appears in `route_trace.jsonl`.
- Docs explain what may be logged: hashes, ids, gate reports, latency/cost.

Patch prompt:

```text
Add a trace privacy guard test and short docs. The trace may contain hashes, ids, gate reasons, latency, and cost, but not raw prompts or raw model outputs. Keep patch small.
```

## 6. Standard patch prompt wrapper

Use this wrapper around any task card:

```text
You are helping with a small open-source Python PoC for local/open-weight inference routing.

Do not expand the project vision.
Do not add token/economy/hype language.
Do not rename the project.
Do not rewrite the architecture.
Do not add unnecessary dependencies.
Make the smallest useful patch.

Repo:
https://github.com/sherlockholmesyes/godworks-open-weights-network

Task:
<PASTE ONE TASK CARD HERE>

Constraints:
- Python >=3.10
- stdlib-first
- unittest tests
- existing demo must keep working
- do not log raw prompts or raw outputs

Output:
1. brief summary
2. files changed
3. test command
4. unified diff
5. risks or assumptions
```

## 7. Contributor response template

Ask contributors to respond with:

```text
Task ID:
Summary:
Files changed:
Test command:
Test result:
Prompt/output privacy check:
Diff or PR link:
Risks/assumptions:
```

## 8. Review checklist

Before accepting a patch, verify:

- [ ] Patch stays inside task scope.
- [ ] Tests added or updated.
- [ ] Demo still runs.
- [ ] No raw prompt/output logs.
- [ ] No token/economy/fundraising language.
- [ ] No hype/revolution claims.
- [ ] No dependency added without clear reason.
- [ ] Objects remain easy to serialize.
- [ ] Error paths are tested.
- [ ] README remains moderator-safe.

## 9. Suggested GitHub labels

- `small-brick`
- `good-first-patch`
- `trace`
- `backend-adapter`
- `schema`
- `node-daemon`
- `privacy`
- `tests-needed`
- `do-not-broaden-scope`

## 10. Suggested Reddit reply for task distribution

```text
Task for you: GOWN-004  make the demo write route_trace.jsonl.

Scope:
- add a tiny trace writer
- write one JSONL line per routed task
- store task hash, candidate nodes, gate reports, chosen node/model, latency/cost
- do not store raw prompt or raw output
- add a unittest that fails if the prompt text appears in the trace

Output a small diff, test command, and assumptions. No architecture rewrite.
```
