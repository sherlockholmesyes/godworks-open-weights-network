# Godworks Open Weights Network — Inference Mesh PoC

This repository is the inference-first track for distributed open-weight model serving.

```text
GOWN = Godworks Open Weights Network
```

Goal:

```text
make open/open-weight models usable through a people-powered inference mesh before attempting distributed training
```

## Root design choice

### Option A

```text
open weights = download a model and run it alone
```

Why not: local-only execution does not create shared access, routing, availability, or a public alternative to closed APIs.

### Option B

```text
open weights network = one central hosted API for open models
```

Why not: a central API recreates the corporate dependency layer.

### Chosen direction

```text
open weights network = decentralized inference mesh with verifiable routing, node reputation, privacy levels, and OpenAI-compatible access
```

## PoC loop

```text
InferenceTask → NodeRegistry → Router → Health/Privacy/Capability gates → chosen NodeCard → InferenceReply
```

## Quick start

```bash
python -m gown_poc.demo
make demo
python -m unittest discover -s tests
make test
```

The demo is stdlib-only. It builds a few mock nodes, rejects nodes that are unhealthy, incompatible, too weak, or privacy-ineligible, and selects an appropriate 12GB-friendly inference node.

## Difference from training track

```text
training track: training/growth of experts
GOWN: running and routing open-weight inference
```

GOWN should become the practical user-facing layer first. A future training track can later feed new experts/models into it.

## Next step

Build the first real local node adapter:

```text
llama.cpp or vLLM backend
+ NodeCard manifest
+ /v1/chat/completions-compatible gateway
+ signed health reports
+ route trace logging
```
