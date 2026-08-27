import pytest

from app.providers.base import BaseProvider
from app.providers.factory import get_provider
from app.providers.mock import MockProvider


def test_factory_returns_provider():
    provider = get_provider()

    assert isinstance(provider, BaseProvider)


def test_factory_returns_mock_provider():
    provider = get_provider()

    assert isinstance(provider, MockProvider)


@pytest.mark.asyncio
async def test_provider_health():
    provider = get_provider()

    result = await provider.health()

    assert result is True


@pytest.mark.asyncio
async def test_mock_chat_does_not_run_inference():
    provider = get_provider()

    result = await provider.chat(
        model="deepseek-coder-local",
        messages=[
            {
                "role": "user",
                "content": "Hello",
            }
        ],
    )

    assert "Mock provider response" in result