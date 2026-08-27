from fastapi import APIRouter

from app.core.health_service import (
    check_provider_health,
)

router = APIRouter(
    prefix="/api",
    tags=["health"],
)


@router.get("/provider-health")
async def provider_health():
    return await check_provider_health()