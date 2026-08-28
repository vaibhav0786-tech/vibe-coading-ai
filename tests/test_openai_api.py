from fastapi.testclient import TestClient

from app.main import app


def test_openai_chat_completions_uses_router_and_mock_provider():
    client = TestClient(app)

    response = client.post(
        "/v1/chat/completions",
        json={
            "model": "qwen2.5-coder:7b",
            "messages": [
                {
                    "role": "user",
                    "content": "Write a Python function that adds two numbers.",
                }
            ],
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert {"id", "object", "model", "choices"} <= data.keys()
    assert data["object"] == "chat.completion"
    assert data["model"] == "qwen2.5-coder:7b"
    assert data["choices"][0]["message"] == {
        "role": "assistant",
        "content": (
            "Mock provider response. "
            "Model execution is disabled during local setup."
        ),
    }
