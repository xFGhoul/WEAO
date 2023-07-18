import logging

from typing import Optional, Tuple, Self, Any
from aiohttp import ClientSession

from .http import Route, HTTP
from .status import Status
from .roblox import Roblox

__all__: Tuple[str, ...] = ("Client",)

logger = logging.getLogger(__name__)


class Client:
    """
    Client Interfact For Innteracting With WEAO API

    Parameters
    -----------
    session: Optional[aiohttp.ClientSession]
        Client Session Used For HTTP Requests
    use_alternative_api: Optional[:class:`bool`]
        Whether To Use Alternative API URL
    """

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        self._http = HTTP(session=session)

    async def __aenter__(self) -> Self:
        if self._http.session is None:
            await self._http.create_client_session()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.cleanup()

    async def cleanup(self) -> None:
        """Closes The Current Client Session

        Raises
        ------
        RuntimeError
            If The Session Was Already Closed
        """
        if self._http.session.closed:
            raise RuntimeError("Client Session Already Closed.")
        logger.debug("Closing Session")
        await self._http.session.close()
        logger.debug("Session Closed")

    async def get_status(self) -> Status:
        """
        Get Status of All Exploits


        Returns
        -------
        Status
            Object Representing Status of All Exploits
        """
        data = await self._http.request(Route("GET", "status"))
        return Status(data["Data"])

    async def get_roblox(self) -> Roblox:
        """
        Get Roblox Status For All Platforms


        Returns
        -------
        Roblox
            Object Representing Roblox On Windows, Mac and Mobile
        """
        data = await self._http.request(Route("GET", "status"))
        return Roblox(data["ROBLOX"])
