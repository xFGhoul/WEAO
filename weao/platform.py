from typing import Dict, Tuple

__all__: Tuple[str, ...] = (
    "Platform",
    "Byfron",
    "Mac",
    "Windows",
    "Android",
)


class Platform:
    def __init__(self, data: Dict) -> None:
        self.byfron: Byfron = Byfron(data.get("Byfron"))
        self.mac: Mac = Mac(data.get("Mac"))
        self.windows: Windows = Windows(data.get("Windows"))


class Byfron:
    def __init__(self, data: Dict) -> None:
        self.status: int = data.get("status")
        self.version: str = data.get("exp_ver")
        self.roblox_version: str = data.get("rbx_ver")
        self.is_free: bool = data.get("is_free")
        self.last_update: int = data.get("upd_unix")


class Mac:
    def __init__(self, data: Dict) -> None:
        self.status: int = data.get("status")
        self.version: str = data.get("exp_ver")
        self.roblox_version: str = data.get("rbx_ver")
        self.is_free: bool = data.get("is_free")
        self.last_update: int = data.get("upd_unix")


class Windows:
    def __init__(self, data: Dict) -> None:
        self.status: int = data.get("status")
        self.version: str = data.get("exp_ver")
        self.roblox_version: str = data.get("rbx_ver")
        self.is_free: bool = data.get("is_free")
        self.last_update: int = data.get("upd_unix")


class Android:
    def __init__(self, data: Dict) -> None:
        self.status: int = data.get("status")
        self.version: str = data.get("exp_ver")
        self.roblox_version: str = data.get("rbx_ver")
        self.is_free: bool = data.get("is_free")
        self.last_update: int = data.get("upd_unix")
