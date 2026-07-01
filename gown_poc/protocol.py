from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ModelCard:
    model_id: str
    weight_hash: str
    quantization: str
    context_tokens: int
    capabilities: tuple[str, ...]
    license: str
    vram_min_gb: int

    def supports(self, task: "InferenceTask") -> bool:
        if self.context_tokens < task.min_context_tokens:
            return False
        return all(cap in self.capabilities for cap in task.required_capabilities)


@dataclass(frozen=True)
class NodeCard:
    node_id: str
    endpoint: str
    gpu_name: str
    vram_gb: int
    models: tuple[ModelCard, ...]
    health_score: float
    trust_level: str
    privacy_modes: tuple[str, ...]
    avg_latency_ms: int
    cost_units: float
    signature: str = ""

    def supports(self, task: "InferenceTask") -> bool:
        return any(self.vram_gb >= model.vram_min_gb and model.supports(task) for model in self.models)


@dataclass(frozen=True)
class InferenceTask:
    task_id: str
    prompt: str
    required_capabilities: tuple[str, ...]
    min_context_tokens: int = 2048
    privacy_level: str = "public"
    max_latency_ms: int = 10000
    max_cost_units: float = 0.0


@dataclass(frozen=True)
class InferenceReply:
    task_id: str
    node_id: str
    model_id: str
    text: str
    latency_ms: int
    cost_units: float
    signature: str


@dataclass(frozen=True)
class GateConfig:
    min_health_score: float = 0.80
    require_signature: bool = True
    allowed_trust_for_restricted: tuple[str, ...] = ("trusted", "local")


@dataclass(frozen=True)
class GateReport:
    node_id: str
    accepted: bool
    score: float
    reasons: tuple[str, ...]


class NodeRegistry:
    def __init__(self) -> None:
        self._nodes: dict[str, NodeCard] = {}

    def register(self, node: NodeCard) -> None:
        if node.node_id in self._nodes:
            raise ValueError(f"duplicate node_id: {node.node_id}")
        self._nodes[node.node_id] = node

    def search(self, task: InferenceTask) -> list[NodeCard]:
        return [node for node in self._nodes.values() if node.supports(task)]


class Router:
    def __init__(self, registry: NodeRegistry, config: GateConfig | None = None) -> None:
        self.registry = registry
        self.config = config or GateConfig()

    def evaluate_node(self, node: NodeCard, task: InferenceTask) -> GateReport:
        reasons: list[str] = []
        if node.health_score < self.config.min_health_score:
            reasons.append("health below threshold")
        if task.privacy_level not in node.privacy_modes:
            reasons.append("privacy mode unsupported")
        if task.privacy_level != "public" and node.trust_level not in self.config.allowed_trust_for_restricted:
            reasons.append("node trust too low for restricted task")
        if node.avg_latency_ms > task.max_latency_ms:
            reasons.append("latency above budget")
        if task.max_cost_units and node.cost_units > task.max_cost_units:
            reasons.append("cost above budget")
        if self.config.require_signature and not node.signature:
            reasons.append("missing signature")

        accepted = not reasons
        score = node.health_score + len(task.required_capabilities) - node.avg_latency_ms / max(task.max_latency_ms, 1) - node.cost_units
        if accepted:
            reasons.append("accepted: inference gates passed")
        return GateReport(node.node_id, accepted, round(score, 6), tuple(reasons))

    def route(self, task: InferenceTask) -> tuple[NodeCard | None, list[GateReport]]:
        candidates = self.registry.search(task)
        reports = [self.evaluate_node(node, task) for node in candidates]
        accepted_ids = {report.node_id for report in reports if report.accepted}
        nodes = [node for node in candidates if node.node_id in accepted_ids]
        if not nodes:
            return None, reports
        by_id = {report.node_id: report for report in reports}
        nodes.sort(key=lambda node: by_id[node.node_id].score, reverse=True)
        return nodes[0], reports

    def call(self, task: InferenceTask, node: NodeCard) -> InferenceReply:
        model = next(model for model in node.models if model.supports(task))
        return InferenceReply(
            task_id=task.task_id,
            node_id=node.node_id,
            model_id=model.model_id,
            text=f"PoC inference reply from {node.node_id} using {model.model_id}.",
            latency_ms=node.avg_latency_ms,
            cost_units=node.cost_units,
            signature=f"reply:{node.node_id}:{task.task_id}",
        )
