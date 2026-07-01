# GOWN Technology Stack — design

## Root

Option A:

```text
GOWN is just an inference server
```

Why not: an inference server does not provide routing, node cards, health gates, traces, or reputation.

Option B:

```text
GOWN must invent a new model runtime
```

Why not: runtime invention delays the mesh.

Chosen direction:

```text
GOWN is a thin mesh protocol over existing open-weight runtimes
```

## Base technologies

### Artifact and protocol layer

```text
JSON Schema for ModelCard and NodeCard
content hashes for weights
route_trace.jsonl for routing evidence
sqlite for local registry/reputation first
```

### Inference backends

```text
llama.cpp for consumer GPU/CPU quantized nodes
vLLM for high-throughput GPU nodes
SGLang for structured generation nodes
ONNX/TensorRT path later only if useful
```

### Gateway layer

```text
small HTTP server
chat-compatible request shape
model list
node list
route explanation
health endpoint
```

### Node daemon

```text
gown node profile
gown node serve
gown node health
gown node trace
gown node register
```

### Routing gates

```text
capability match
context length fit
VRAM fit
health score
routing mode
latency budget
cost budget
fallback policy
```

### Trust and operations

```text
node identity
signed node card
health probes
canary tasks
rate limits
quarantine state
reputation score
```

## First implementation target

```text
one local llama.cpp adapter
one ModelCard
one NodeCard
one router call
one route_trace.jsonl
one smoke test
```

## Training bridge

```text
A future training track produces admitted experts.
GOWN serves admitted experts.
Shared cards and traces allow the two systems to connect without becoming one repo.
```

## Next step

```text
replace mock reply with real local model call and write the route trace to disk
```
