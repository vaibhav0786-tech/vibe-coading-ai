from fastapi import APIRouter

from app.api.schemas import ChatRequest, ChatResponse
from app.routing.router import route_request

router = APIRouter(
    prefix="/api",
    tags=["chat"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest):

    user_message = request.messages[-1].content

    decision = route_request(user_message)

    return ChatResponse(
        task_type=decision.task_type,
        model=decision.model.name,
        confidence=decision.confidence,
        status="routing_only",
        message=(
            "Request classified successfully. "
            "Model execution is disabled during setup."
        ),
    )