class GatewayError(Exception):
    """Base gateway exception."""


class ProviderUnavailableError(GatewayError):
    """Provider cannot be reached."""


class ModelUnavailableError(GatewayError):
    """Requested model is unavailable."""


class RoutingError(GatewayError):
    """Routing failed."""