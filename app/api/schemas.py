from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str = Field(
        ...,
        description="Message role: system, user, or assistant",
    )

    content: str = Field(
        ...,
        min_length=1,
    )


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(
        ...,
        min_length=1,
    )


class ChatResponse(BaseModel):
    task_type: str
    model: str
    confidence: float
    status: str
    message: str