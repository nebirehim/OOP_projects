from enum import Enum
from typing import Type


class AppBaseException(Exception):
    """Base class for all application exceptions."""
    pass


class ConnectionException(AppBaseException):
    """Custom exception for connection-related errors."""
    pass


class ValueErrorException(AppBaseException):
    """Custom exception for value-related errors."""
    pass


class AppException(Enum):
    # Define exceptions as enumeration members
    Timeout = (100, ConnectionException, "Timeout connecting to resource")
    NotAnInteger = (200, ValueErrorException, "Value is not an integer")

    def __init__(self, code: int, exception_type: Type[AppBaseException], default_message: str):
        self._code = code
        self._exception_type = exception_type
        self._default_message = default_message

    @property
    def code(self) -> int:
        """Get the error code."""
        return self._code

    @property
    def exception_type(self) -> Type[AppBaseException]:
        """Get the exception class/type."""
        return self._exception_type

    @property
    def message(self) -> str:
        """Get the default message."""
        return self._default_message

    def throw(self, custom_message: str = None) -> None:
        """
        Raise the exception with either the default message or a custom one.
        
        Args:
            custom_message (str, optional): Custom message for the exception.
        """
        message = custom_message if custom_message else self._default_message
        raise self._exception_type(f"{self._code} - {message}")

    @classmethod
    def list_exceptions(cls) -> list:
        """
        List all possible exceptions defined in the enum.

        Returns:
            list: A list of tuples containing (code, exception type, message).
        """
        return [(exc.code, exc.exception_type.__name__, exc.message) for exc in cls]


# Example Usage
try:
    AppException.Timeout.throw()
except AppBaseException as e:
    print(f"Caught exception: {e}")

try:
    AppException.NotAnInteger.throw("Invalid integer format")
except AppBaseException as e:
    print(f"Caught exception: {e}")

# List all exceptions
for exc in AppException.list_exceptions():
    print(exc)
