# GOWN Missing Bricks — design

## Root

Option A:

```text
open weights = local-only files
```

Why not: local files do not create a shared inference layer.

Option B:

```text
open weights network = one hosted service
```

Why not: one host recreates central dependency.

Chosen direction:

```text
open weights network = distributed inference mesh
```

## Bricks

### 1. ModelCard

Option A: model is a filename.
Option B: model is a score.
Chosen direction: model is a runnable contract.

Needs:

```text
model_id, weight_hash, quantization, context_tokens, capabilities, license, vram_min_gb, backend
```

### 2. NodeCard

Option A: node is an endpoint.
Option B: node is social trust.
Chosen direction: node is a signed worker card.

Needs:

```text
node_id, endpoint, gpu, vram, model list, health, trust level, routing modes, latency, cost, signature
```

### 3. Router

Option A: router is round-robin.
Option B: router is hidden central policy.
Chosen direction: router is an open policy engine.

Needs:

```text
capability match, context fit, health gate, routing mode gate, latency budget, cost budget, fallback policy
```

### 4. Node daemon

Option A: daemon only serves text.
Option B: daemon is a full platform from day one.
Chosen direction: daemon starts as profile + serve + health report.

Needs:

```text
profile, serve, health, signed report, backend adapter
```

### 5. RouteTrace

Option A: trace is debug logs.
Option B: trace is full prompt dump.
Chosen direction: trace is minimal routing evidence.

Needs:

```text
task_hash, router_version, candidates, chosen_node, model_id, gate_reports, latency, cost, routing_mode
```

### 6. Reputation / Credits

Option A: volunteers scale forever.
Option B: token first.
Chosen direction: reputation and compute credits first.

Needs:

```text
node_score, job_count, failure_count, latency_history, credit_balance
```

## Next step

```text
make one real local backend adapter and write route_trace.jsonl
```
