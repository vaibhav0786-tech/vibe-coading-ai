from app.providers.base import BaseProvider
from app.providers.mock import MockProvider


def get_provider() -> BaseProvider:
    """
    Return the configured AI provider.

    For local development we use MockProvider.
    The real Ollama/cloud provider will be added later.
    """

    return MockProvider()