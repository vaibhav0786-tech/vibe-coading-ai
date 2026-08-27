from dataclasses import dataclass

from app.models.registry import ModelDefinition, get_model
from app.routing.classifier import Classification, classify_task


@dataclass(frozen=True)
class RoutingDecision:
    task_type: str
    model: ModelDefinition
    confidence: float
    reason: str


def route_request(prompt: str) -> RoutingDecision:
    classification: Classification = classify_task(prompt)

    model = get_model(classification.task_type)

    return RoutingDecision(
        task_type=classification.task_type,
        model=model,
        confidence=classification.confidence,
        reason=classification.reason,
    )