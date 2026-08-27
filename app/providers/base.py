from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract interface for AI model providers.

    Local Ollama, cloud Ollama, LiteLLM, or another
    provider can implement this interface later.
    """

    @abstractmethod
    async def health(self) -> bool:
        """Return True when the provider is reachable."""
        raise NotImplementedError

    @abstractmethod
    async def chat(
        self,
        model: str,
        messages: list[dict],
    ) -> str:
        """Send a chat request to the provider."""
        raise NotImplementedError