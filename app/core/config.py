import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")

    app_host: str = os.getenv("APP_HOST", "127.0.0.1")
    app_port: int = int(os.getenv("APP_PORT", "9000"))

    model_provider: str = os.getenv("MODEL_PROVIDER", "ollama")

    ollama_base_url: str = os.getenv(
        "OLLAMA_BASE_URL",
        "http://127.0.0.1:11434",
    )

    ollama_cloud_url: str = os.getenv(
        "OLLAMA_CLOUD_URL",
        "",
    )

    model_endpoint: str = os.getenv(
        "MODEL_ENDPOINT",
        "local",
    )

    coding_model: str = os.getenv(
        "CODING_MODEL",
        "qwen2.5-coder:7b",
    )

    reasoning_model: str = os.getenv(
        "REASONING_MODEL",
        "qwen2.5-coder:7b",
    )

    vision_model: str = os.getenv(
        "VISION_MODEL",
        "qwen2.5-coder:7b",
    )

    request_timeout_seconds: int = int(
        os.getenv("REQUEST_TIMEOUT_SECONDS", "600")
    )

    log_level: str = os.getenv(
        "LOG_LEVEL",
        "INFO",
    )


settings = Settings()
