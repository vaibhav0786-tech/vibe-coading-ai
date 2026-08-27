from app.providers.factory import get_provider


def test_provider_creation():
    provider = get_provider()

    assert provider is not None