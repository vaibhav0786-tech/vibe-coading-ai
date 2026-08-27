from app.routing.fallback_router import (
    get_fallback_chain,
)


def test_coding_fallback_chain():
    chain = get_fallback_chain("coding")

    assert len(chain) >= 1
    assert chain[0] == "deepseek-coder-local"


def test_reasoning_fallback_chain():
    chain = get_fallback_chain("reasoning")

    assert chain[0] == "qwen3-thinking-local"


def test_unknown_chain():
    chain = get_fallback_chain("unknown")

    assert chain[0] == "qwen3-thinking-local"