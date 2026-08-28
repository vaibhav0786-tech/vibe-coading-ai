import pytest

from app.providers.ollama import OllamaProvider


@pytest.mark.integration
@pytest.mark.asyncio
async def test_ollama_chat_with_installed_coding_model():
    provider = OllamaProvider()

    if not await provider.health():
        pytest.skip("Ollama is not reachable at OLLAMA_BASE_URL")

    response = await provider.chat(
        model="qwen2.5-coder:7b",
        messages=[
            {
                "role": "user",
                "content": "Reply with the word 'ready'.",
            }
        ],
    )

    assert isinstance(response, str)
    assert response.strip()
