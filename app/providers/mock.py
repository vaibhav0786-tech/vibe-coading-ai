from app.providers.base import BaseProvider


class MockProvider(BaseProvider):
    """
    Safe development provider.

    This provider never performs model inference.
    It exists so the gateway can be developed and
    tested before connecting a cloud GPU.
    """

    async def health(self) -> bool:
        return True

    async def chat(
        self,
        model: str,
        messages: list[dict],
    ) -> str:
        return (
            "Mock provider response. "
            "Model execution is disabled during local setup."
        )