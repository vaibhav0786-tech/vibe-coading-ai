from app.routing.fallback_router import (
    get_fallback_chain,
)


def test_no_fallback_models_are_configured():
    assert get_fallback_chain("coding") == []
    assert get_fallback_chain("reasoning") == []
    assert get_fallback_chain("vision") == []


def test_unknown_task_has_no_fallback_chain():
    assert get_fallback_chain("unknown") == []
