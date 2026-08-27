from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.health import router as health_router
from app.core.logging_config import configure_logging

logger = configure_logging()

app = FastAPI(
    title="Vibe Coding AI Gateway",
    version="0.1.0",
    description="Cloud-ready AI coding orchestration gateway",
)

app.include_router(chat_router)
app.include_router(health_router)


@app.get("/health")
async def health():
    logger.info("Health check requested")

    return {
        "status": "ok",
        "service": "vibe-coding-gateway",
    }


@app.get("/")
async def root():
    return {
        "name": "Vibe Coding AI Gateway",
        "version": "0.1.0",
    }