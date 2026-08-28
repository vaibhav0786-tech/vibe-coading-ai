from fastapi import APIRouter, HTTPException

from app.api.schemas import ChatRequest, ChatResponse
from app.providers.factory import get_provider
from app.routing.router import RoutingDecision, route_request

router = APIRouter(
    prefix="/api",
    tags=["chat"],
)


async def execute_chat(
    request: ChatRequest,
) -> tuple[RoutingDecision, str]:
    user_message = request.messages[-1].content
    decision = route_request(user_message)
    provider = get_provider()

    messages = [
        message.model_dump()
        for message in request.messages
    ]
    response = await provider.chat(
        model=decision.model.name,
        messages=messages,
    )

    return decision, response


@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest):
    try:
        decision, response = await execute_chat(request)
    except (RuntimeError, ValueError) as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Model provider error: {exc}",
        ) from exc

    return ChatResponse(
        task_type=decision.task_type,
        model=decision.model.name,
        confidence=decision.confidence,
        status="completed",
        message=response,
    )
