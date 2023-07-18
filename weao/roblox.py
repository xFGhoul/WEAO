from typing import Tuple, Dict

__all__: Tuple[str, ...] = (
    "Roblox",
    "RobloxPlatform",
    "RobloxWindows",
    "RobloxMac",
    "RobloxMobile",
)


class Roblox:
    """
    Class Interface Containing Roblox Attributes

    Attributes
    ----------
    windows: :class:`RobloxWindows`
        Roblox Windows
    mac: :class:`RobloxMac`
        Roblox Mac
    mobile: :class:`RobloxMobile`
        Roblox Mobile
    """

    __slots__: Tuple[str, ...] = (
        "mobile",
        "windows",
        "mac",
    )

    def __init__(self, data: Dict) -> None:
        self.mobile = RobloxMobile(data[0])
        self.windows = RobloxWindows(data[1])
        self.mac = RobloxMac(data[2])


class RobloxPlatform:
    """
    Class Interface Containing Roblox Attributes For Specific Platform

    Attributes
    ----------
    player: :class:`str`
        The Kind Of Platform
    version: :class:`str`
        Current Version of Roblox
    last_update: :class:`int`
        Last update of Exploit in Unix Time
    """

    __slots__: Tuple[str, ...] = ("player", "version", "last_update")

    def __init__(self, data: Dict) -> None:
        self.player = data.get("Player")
        self.version = data.get("ver")
        self.last_update = data.get("upd_unix")


class RobloxWindows(RobloxPlatform):
    ...


class RobloxMac(RobloxPlatform):
    ...


class RobloxMobile(RobloxPlatform):
    ...
