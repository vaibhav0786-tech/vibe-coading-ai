from app.routing.router import route_request


def test_code_routes_to_coding_model():
    decision = route_request(
        "Write a Python function to parse JSON"
    )

    assert decision.task_type == "coding"
    assert decision.model.name == "deepseek-coder-local"


def test_reasoning_routes_to_reasoning_model():
    decision = route_request(
        "Analyze the architecture and explain the tradeoffs"
    )

    assert decision.task_type == "reasoning"
    assert decision.model.name == "qwen3-thinking-local"


def test_disabled_vision_model_fails_safely():
    try:
        route_request(
            "Analyze this screenshot"
        )
    except RuntimeError as error:
        assert "vision" in str(error).lower()
    else:
        raise AssertionError(
            "Expected disabled vision model to raise RuntimeError"
        )