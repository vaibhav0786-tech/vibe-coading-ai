from app.routing.classifier import classify_task


def test_code_task():
    result = classify_task(
        "Fix this Python function and debug the API"
    )

    assert result.task_type == "coding"


def test_reasoning_task():
    result = classify_task(
        "Analyze the architecture and explain the best approach"
    )

    assert result.task_type == "reasoning"


def test_vision_task():
    result = classify_task(
        "Analyze this screenshot and explain what is wrong"
    )

    assert result.task_type == "vision"


def test_unknown_task_defaults_to_reasoning():
    result = classify_task(
        "Tell me something interesting"
    )

    assert result.task_type == "reasoning"