from typing import Tuple, Dict

from .exploit import (
    Synapse,
    ScriptWare,
    Krnl,
    Dx9Ware,
    Electron,
    WeAreDevs,
    OxygenU,
    Fluxus,
    Celestial,
    Comet,
    Elexe,
    Hydrogen,
)

__all__: Tuple[str, ...] = ("Status",)


class Status:
    """
    Class Interface Containing User Attributes

    Attributes
    ----------
    synapse: :class:Synapse
        Synapse Exploit Status
    script_ware: :class:ScriptWare
        Script Ware Exploit Status
    krnl: :class:Krnl
        KRNL Exploit Status
    dx9ware: :class:Dx9Ware
        DX9WARE Exploit Status
    electron: :class:Electron
        Electron Exploit Status
    wearedevs_api: :class:WeAreDevs
        We Are Devs API Exploit Status
    oxygen: :class:OxygenU
        Oxygen-U Exploit Status
    fluxus: :class:Fluxus
        Fluxus Exploit Status
    celestial: :class:Celestial
        Celestial Exploit Status
    comet: :class:Comet
        Comet Exploit Status
    elexe: :class:Elexe
        Elexe Exploit Status
    hydrogen: :class:Hydrogen
        Hydrogen Exploit Status
    """

    __slots__: Tuple[str, ...] = (
        "synapse",
        "script_ware",
        "krnl",
        "dx9ware",
        "electron",
        "wearedevs_api",
        "oxygen",
        "fluxus",
        "celestial",
        "comet",
        "elexe",
        "hydrogen",
    )

    def __init__(self, data: Dict) -> None:
        self.synapse: Synapse = Synapse(data.get("Synapse"))
        self.script_ware: ScriptWare = ScriptWare(data.get("Script-Ware"))
        self.krnl: Krnl = Krnl(data.get("KRNL"))
        self.dx9ware: Dx9Ware = Dx9Ware(data.get("DX9WARE"))
        self.electron: Electron = Electron(data.get("Electron"))
        self.wearedevs_api: WeAreDevs = WeAreDevs(data.get("WeAreDevs API"))
        self.oxygen: OxygenU = OxygenU(data.get("Oxygen-U"))
        self.fluxus: Fluxus = Fluxus(data.get("Fluxus"))
        self.celestial: Celestial = Celestial(data.get("Celestial"))
        self.comet: Comet = Comet(data.get("Comet"))
        self.elexe: Elexe = Elexe(data.get("Elexe"))
        self.hydrogen: Hydrogen = Hydrogen(data.get("Hydrogen"))

    def __repr__(self) -> str:
        return "<Status>"
