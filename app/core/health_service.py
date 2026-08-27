from app.providers.factory import get_provider


async def check_provider_health() -> dict:
    provider = get_provider()

    healthy = await provider.health()

    return {
        "provider": provider.__class__.__name__,
        "healthy": healthy,
    }