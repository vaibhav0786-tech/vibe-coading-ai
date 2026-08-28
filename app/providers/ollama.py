import httpx

from app.core.config import settings
from app.providers.base import BaseProvider


class OllamaProvider(BaseProvider):
    """
    Ollama provider for local or cloud-hosted Ollama servers.
    """

    def __init__(self, base_url: str | None = None):
        self.base_url = (
            base_url or settings.ollama_base_url
        ).rstrip("/")

        self.timeout = settings.request_timeout_seconds

    async def health(self) -> bool:
        """
        Check whether the Ollama API is reachable.
        """
        try:
            async with httpx.AsyncClient(
                timeout=10
            ) as client:
                response = await client.get(
                    f"{self.base_url}/api/tags"
                )

                return response.is_success

        except httpx.HTTPError:
            return False

    async def chat(
        self,
        model: str,
        messages: list[dict],
    ) -> str:
        """
        Send a chat request to Ollama.
        """
        payload = {
            "model": model,
            "messages": messages,
            "stream": False,
        }

        try:
            async with httpx.AsyncClient(
                timeout=self.timeout
            ) as client:
                response = await client.post(
                    f"{self.base_url}/api/chat",
                    json=payload,
                )

                response.raise_for_status()

                data = response.json()

                return data["message"]["content"]

        except httpx.HTTPError as exc:
            raise RuntimeError(
                f"Ollama request failed: {exc}"
            ) from exc

        except (KeyError, TypeError) as exc:
            raise RuntimeError(
                "Ollama returned an unexpected response."
            ) from exc