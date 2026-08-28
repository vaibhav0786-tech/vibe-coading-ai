from dataclasses import dataclass


@dataclass(frozen=True)
class ModelDefinition:
    name: str
    role: str
    capabilities: tuple[str, ...]
    enabled: bool = True


MODELS = {
    "coding": ModelDefinition(
        name="qwen2.5-coder:7b",
        role="coding",
        capabilities=(
            "code_generation",
            "code_review",
            "debugging",
            "refactoring",
        ),
    ),
    "reasoning": ModelDefinition(
        name="qwen2.5-coder:7b",
        role="reasoning",
        capabilities=(
            "reasoning",
            "planning",
            "analysis",
        ),
    ),
    "vision": ModelDefinition(
        name="qwen2.5-coder:7b",
        role="vision",
        capabilities=(),
        enabled=False,
    ),
}


def get_model(task_type: str) -> ModelDefinition:
    try:
        model = MODELS[task_type]
    except KeyError as exc:
        raise ValueError(
            f"Unknown task type: {task_type}"
        ) from exc

    if not model.enabled:
        raise RuntimeError(
            f"Model for task '{task_type}' is disabled"
        )

    return model
