from fastapi import APIRouter, HTTPException

from app.api.chat import execute_chat
from app.api.schemas import ChatRequest

router = APIRouter(
    prefix="/v1",
    tags=["openai"],
)


@router.post("/chat/completions")
async def chat_completions(request: ChatRequest):
    try:
        decision, response = await execute_chat(request)
    except (RuntimeError, ValueError) as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Model provider error: {exc}",
        ) from exc

    return {
        "id": "vibe-coding-chat",
        "object": "chat.completion",
        "model": decision.model.name,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": response,
                },
                "finish_reason": "stop",
            }
        ],
    }
