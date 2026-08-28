import pytest

from app.routing.router import route_request


def test_code_routes_to_coding_model():
    decision = route_request(
        "Write a Python function to parse JSON"
    )

    assert decision.task_type == "coding"
    assert decision.model.name == "qwen2.5-coder:7b"


def test_reasoning_routes_to_reasoning_model():
    decision = route_request(
        "Analyze the architecture and explain the tradeoffs"
    )

    assert decision.task_type == "reasoning"
    assert decision.model.name == "qwen2.5-coder:7b"


def test_vision_is_disabled_until_vision_model_is_installed():
    with pytest.raises(
        RuntimeError,
        match="Model for task 'vision' is disabled",
    ):
        route_request(
            "Analyze this screenshot and explain what is wrong"
        )