from dataclasses import dataclass


@dataclass(frozen=True)
class ModelDefinition:
    name: str
    role: str
    capabilities: tuple[str, ...]
    enabled: bool = True


MODELS = {
    "coding": ModelDefinition(
        name="deepseek-coder-local",
        role="coding",
        capabilities=(
            "code_generation",
            "code_review",
            "debugging",
            "refactoring",
        ),
    ),

    "reasoning": ModelDefinition(
        name="qwen3-thinking-local",
        role="reasoning",
        capabilities=(
            "reasoning",
            "planning",
            "analysis",
        ),
    ),

    "vision": ModelDefinition(
        name="devstral-vision-local",
        role="vision",
        capabilities=(
            "image_analysis",
            "multimodal",
            "visual_coding",
        ),
        enabled=False,
    ),
}


def get_model(task_type: str) -> ModelDefinition:
    try:
        model = MODELS[task_type]
    except KeyError:
        raise ValueError(
            f"Unknown task type: {task_type}"
        )

    if not model.enabled:
        raise RuntimeError(
            f"Model for task '{task_type}' is disabled"
        )

    return model