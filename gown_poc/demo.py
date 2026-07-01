from __future__ import annotations

from .protocol import InferenceTask, ModelCard, NodeCard, NodeRegistry, Router


def build_registry() -> NodeRegistry:
    coder_7b = ModelCard(
        model_id="open-coder-7b-q4-demo",
        weight_hash="sha256:open-coder-7b-demo",
        quantization="q4_k_m",
        context_tokens=8192,
        capabilities=("chat", "code", "python"),
        license="research-demo",
        vram_min_gb=8,
    )
    general_8b = ModelCard(
        model_id="open-general-8b-q4-demo",
        weight_hash="sha256:open-general-8b-demo",
        quantization="q4_k_m",
        context_tokens=4096,
        capabilities=("chat", "general"),
        license="research-demo",
        vram_min_gb=8,
    )

    registry = NodeRegistry()
    registry.register(
        NodeCard(
            node_id="node_12gb_fast_local",
            endpoint="http://127.0.0.1:8011",
            gpu_name="consumer-12gb-demo",
            vram_gb=12,
            models=(coder_7b, general_8b),
            health_score=0.97,
            trust_level="local",
            privacy_modes=("public", "restricted", "local_only"),
            avg_latency_ms=1700,
            cost_units=0.01,
            signature="sig:node_12gb_fast_local",
        )
    )
    registry.register(
        NodeCard(
            node_id="node_8gb_public_slow",
            endpoint="http://example.invalid:8012",
            gpu_name="consumer-8gb-demo",
            vram_gb=8,
            models=(general_8b,),
            health_score=0.86,
            trust_level="public",
            privacy_modes=("public",),
            avg_latency_ms=9200,
            cost_units=0.005,
            signature="sig:node_8gb_public_slow",
        )
    )
    registry.register(
        NodeCard(
            node_id="node_unhealthy_coder",
            endpoint="http://example.invalid:8013",
            gpu_name="consumer-12gb-demo",
            vram_gb=12,
            models=(coder_7b,),
            health_score=0.41,
            trust_level="public",
            privacy_modes=("public",),
            avg_latency_ms=2100,
            cost_units=0.0,
            signature="sig:node_unhealthy_coder",
        )
    )
    return registry


def main() -> None:
    task = InferenceTask(
        task_id="demo-infer-001",
        prompt="Explain and patch a small Python bug.",
        required_capabilities=("chat", "code", "python"),
        min_context_tokens=4096,
        privacy_level="restricted",
        max_latency_ms=5000,
        max_cost_units=0.05,
    )

    router = Router(build_registry())
    chosen, reports = router.route(task)

    print("GOWN PoC inference routing reports")
    print("=" * 35)
    for report in reports:
        verdict = "ACCEPT" if report.accepted else "REJECT"
        print(f"{verdict:6} {report.node_id:24} score={report.score}")
        for reason in report.reasons:
            print(f"  - {reason}")

    print()
    if chosen is None:
        print("No inference node admitted.")
        return

    reply = router.call(task, chosen)
    print(f"Chosen node: {chosen.node_id}")
    print(f"Reply: {reply.text}")


if __name__ == "__main__":
    main()
