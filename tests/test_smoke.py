import unittest

from gown_poc.demo import build_registry
from gown_poc.protocol import InferenceTask, Router


class SmokeTest(unittest.TestCase):
    def test_demo_route(self) -> None:
        task = InferenceTask(
            task_id="smoke",
            prompt="small python task",
            required_capabilities=("chat", "code", "python"),
            min_context_tokens=4096,
            privacy_level="restricted",
            max_latency_ms=5000,
            max_cost_units=0.05,
        )
        chosen, reports = Router(build_registry()).route(task)
        self.assertTrue(reports)
        self.assertIsNotNone(chosen)
        assert chosen is not None
        self.assertEqual(chosen.node_id, "node_12gb_fast_local")


if __name__ == "__main__":
    unittest.main()
