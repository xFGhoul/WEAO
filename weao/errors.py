from typing import Tuple, Optional, Any, Union, Dict
from aiohttp import ClientResponse

__all__: Tuple[str, ...] = (
    "HTTPException",
    "NotFound",
    "WEAOException",
    "WEAOUnavailable",
)


class WEAOException(Exception):
    """Generic API Exception For WEAO"""

    __slots__: Tuple[str, ...] = ()


class HTTPException(WEAOException):
    """An exception raised when an HTTP Exception occurs from the API.

    Attributes
    ----------
    response: :class:`aiohttp.ClientResponse`
        The response from the API.
    data: :class:`Any`
        The data returned from the API.
    """

    __slots__: Tuple[str, ...] = (
        "response",
        "data",
    )

    def __init__(
        self,
        response: Optional[ClientResponse] = None,
        data: Optional[Union[Dict[Any, Any], Any]] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.response: Optional[ClientResponse] = response
        self.data: Any = data

        self.message: Optional[str] = (
            data.get("error", {}) if isinstance(data, dict) else None
        )

        super().__init__(
            f"{self.message or 'No message'}",
            *args,
            **kwargs,
        )


class NotFound(HTTPException):
    """Raised When Object Could Not Be Found

    This inherits from :class:`HTTPException`.
    """

    __slots__: Tuple[str, ...] = ()


class WEAOUnavailable(HTTPException):
    """Raised When WEAO Servers Fail"""

    __slots__: Tuple[str, ...] = ()
