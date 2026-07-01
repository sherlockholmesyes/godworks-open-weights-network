"""GOWN PoC: Godworks Open Weights Network.

Inference-first mesh skeleton:
InferenceTask -> NodeRegistry -> Router -> gate reports -> InferenceReply.
"""

from .protocol import (
    GateConfig,
    GateReport,
    InferenceReply,
    InferenceTask,
    ModelCard,
    NodeCard,
    NodeRegistry,
    Router,
)

__all__ = [
    "GateConfig",
    "GateReport",
    "InferenceReply",
    "InferenceTask",
    "ModelCard",
    "NodeCard",
    "NodeRegistry",
    "Router",
]
