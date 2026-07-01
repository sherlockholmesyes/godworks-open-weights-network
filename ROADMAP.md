# GOWN Roadmap — design

## Stage 0 — Local inference loop

Option A:

```text
start with public mesh
```

Why not: public networking hides local protocol bugs.

Option B:

```text
start with only docs
```

Why not: no executable pressure.

Chosen direction:

```text
start with local runnable inference loop
```

Build:

```text
NodeCard
ModelCard
InferenceTask
Router
GateReport
mock InferenceReply
```

Acceptance:

```text
demo must route to one valid node and reject bad candidates
```

---

## Stage 1 — Real local backend adapter

Option A:

```text
mock backend is enough
```

Why not: no real model execution.

Option B:

```text
support every backend first
```

Why not: integration sprawl.

Chosen direction:

```text
one real backend adapter first
```

Build:

```text
llama.cpp adapter or vLLM adapter
local model card
health probe
single prompt call
```

Acceptance:

```text
Router.call returns real model output
```

---

## Stage 2 — RouteTrace

Option A:

```text
logs are enough
```

Why not: not replayable.

Option B:

```text
store everything
```

Why not: unnecessary exposure and noise.

Chosen direction:

```text
store minimal routing evidence
```

Build:

```text
route_trace.jsonl
candidate nodes
chosen node
gate reports
latency
cost
routing mode
```

Acceptance:

```text
every routed task writes one trace
```

---

## Stage 3 — Node daemon

Option A:

```text
node = script
```

Why not: no stable service.

Option B:

```text
node = huge platform
```

Why not: too much before proof.

Chosen direction:

```text
node = small daemon with profile, serve, health
```

Build:

```text
gown node profile
gown node serve
gown node health
```

Acceptance:

```text
node can be discovered and selected by router
```

---

## Stage 4 — LAN mesh

Option A:

```text
internet alpha immediately
```

Why not: too many variables.

Option B:

```text
single machine forever
```

Why not: no mesh pressure.

Chosen direction:

```text
2-3 node LAN mesh
```

Build:

```text
registry
heartbeat
task dispatch
fallback on node loss
```

Acceptance:

```text
one node can fail without killing routing
```

---

## Stage 5 — Public alpha

Option A:

```text
public nodes receive all traffic
```

Why not: routing policy failure.

Option B:

```text
only trusted nodes ever participate
```

Why not: no open network.

Chosen direction:

```text
public alpha with staged routing modes
```

Build:

```text
node identity
routing modes
rate limits
reputation score
public registry
```

Acceptance:

```text
unknown nodes only receive tasks permitted by routing policy
```

---

## Stage 6 — Training bridge

Option A:

```text
inference network and training network are separate forever
```

Why not: new experts cannot reach users.

Option B:

```text
training and inference must be one repo/system
```

Why not: mixed responsibilities.

Chosen direction:

```text
GOWN serves admitted model artifacts through shared cards and gates
```

Build:

```text
compatible ExpertCard/ModelCard bridge
admitted training artifact becomes routable GOWN model/expert
shared trace format
```

Acceptance:

```text
Training artifact cannot receive GOWN traffic without serving card and route gates
```
