# GOWN Architecture — design

GOWN is the inference-first track for open-weight models.

```text
OWN = Open Weights Network
```

## Root design choice

### Option A

```text
open weights = local model files only
```

Why not: one machine gains independence, but no shared routing layer exists.

### Option B

```text
open weights network = one hosted service
```

Why not: the access layer becomes centralized again.

### Chosen direction

```text
open weights network = distributed inference mesh
```

Minimal object:

```text
ModelCard + NodeCard + Router + GateReport + RouteTrace
```

## ModelCard

### Option A

```text
model = filename
```

Why not: no runtime contract.

### Option B

```text
model = benchmark score
```

Why not: no serving constraints.

### Chosen direction

```text
model = runnable contract
```

Fields:

```text
model_id
weight_hash
quantization
context_tokens
capabilities
license
vram_min_gb
backend
```

## NodeCard

### Option A

```text
node = endpoint
```

Why not: no resource profile.

### Option B

```text
node = trusted volunteer
```

Why not: not enough for scale.

### Chosen direction

```text
node = signed worker card
```

Fields:

```text
node_id
endpoint
gpu_name
vram_gb
models
health_score
trust_level
routing_modes
latency
cost
signature
```

## Router

### Option A

```text
router = round-robin
```

Why not: ignores capability and context.

### Option B

```text
router = hidden central policy
```

Why not: not forkable.

### Chosen direction

```text
router = open policy engine
```

Uses:

```text
capability match
context fit
health gate
routing mode
latency budget
cost budget
trace output
```

## Missing bricks

```text
1. ModelCard format
2. NodeCard format
3. Node daemon
4. Backend adapters
5. Health probe
6. RouteTrace
7. Registry
8. Reputation score
9. Gateway surface
10. Fallback policy
```

## Next step

```text
replace mock Router.call with one real local backend adapter
```
