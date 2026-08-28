from app.core.config import settings
from app.providers.base import BaseProvider
from app.providers.mock import MockProvider
from app.providers.ollama import OllamaProvider


def get_provider() -> BaseProvider:
    """
    Return the configured AI provider.

    Supported modes:

    - mock: safe local development without inference
    - ollama: real Ollama backend

    The provider is selected through MODEL_PROVIDER
    in the environment configuration.
    """

    if settings.model_provider == "mock":
        return MockProvider()

    if settings.model_provider == "ollama":
        if settings.model_endpoint == "cloud":
            if not settings.ollama_cloud_url:
                raise ValueError(
                    "MODEL_ENDPOINT is 'cloud' but "
                    "OLLAMA_CLOUD_URL is not configured."
                )

            return OllamaProvider(
                settings.ollama_cloud_url
            )

        return OllamaProvider(
            settings.ollama_base_url
        )

    raise ValueError(
        f"Unsupported MODEL_PROVIDER: "
        f"{settings.model_provider}"
    )