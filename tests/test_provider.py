from dataclasses import replace

import pytest

import app.providers.factory as factory
from app.providers.base import BaseProvider
from app.providers.factory import get_provider
from app.providers.mock import MockProvider
from app.providers.ollama import OllamaProvider


def test_factory_returns_provider():
    provider = get_provider()

    assert isinstance(provider, BaseProvider)


def test_factory_returns_mock_provider():
    provider = get_provider()

    assert isinstance(provider, MockProvider)


def test_factory_returns_ollama_provider_when_configured(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr(
        factory,
        "settings",
        replace(
            factory.settings,
            model_provider="ollama",
            model_endpoint="local",
        ),
    )

    assert isinstance(factory.get_provider(), OllamaProvider)


def test_factory_rejects_unknown_provider(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr(
        factory,
        "settings",
        replace(factory.settings, model_provider="unknown"),
    )

    with pytest.raises(ValueError, match="Unsupported MODEL_PROVIDER"):
        factory.get_provider()


@pytest.mark.asyncio
async def test_provider_health():
    provider = get_provider()

    result = await provider.health()

    assert result is True


@pytest.mark.asyncio
async def test_mock_chat_does_not_run_inference():
    provider = get_provider()

    result = await provider.chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "user",
                "content": "Hello",
            }
        ],
    )

    assert result == (
        "Mock provider response. "
        "Model execution is disabled during local setup."
    )
