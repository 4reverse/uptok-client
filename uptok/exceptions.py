
class ClientException(Exception):
    """Base class for exceptions in this module."""
    pass


class RateLimit(ClientException):
    """Raised when rate limit exceeded."""
    pass


class PaymentRequired(ClientException):
    """Raised when payment is required."""
    pass


class BadRequest(ClientException):
    """Raised when is bad request."""
    pass


class Unauthorized(ClientException):
    """Raised when user is not authorized."""
    pass


class AccessDenied(ClientException):
    """Raised when user is not authorized."""
    pass