from app.models.fallbacks import FALLBACK_MODELS


def get_fallback_chain(task_type: str) -> list[str]:
    return FALLBACK_MODELS.get(task_type, [])
