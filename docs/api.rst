.. currentmodule:: weao

API Reference
=============

Client
------

.. attributetable:: Client

.. autoclass:: Client
    :members:
    :exclude-members: _make_request

Models
------

Exploit
~~~~~~~

.. attributetable:: Exploit

.. autoclass:: weao.exploit.Exploit()
    :members:

Status
~~~~~~~

.. attributetable:: Status

.. autoclass:: weao.status.Status()
    :members:

Roblox
~~~~~~~

.. attributetable:: Roblox

.. autoclass:: weao.roblox.Roblox()
    :members:

Exploits
--------

Synapse
~~~~~~~

.. attributetable:: Synapse

.. autoclass:: weao.exploit.Synapse()
    :members:

ScriptWare
~~~~~~~

.. attributetable:: ScriptWare

.. autoclass:: weao.exploit.ScriptWare()
    :members:

Krnl
~~~~~~~

.. attributetable:: Krnl

.. autoclass:: weao.exploit.Krnl()
    :members:

Dx9Ware
~~~~~~~

.. attributetable:: Dx9Ware

.. autoclass:: weao.exploit.Dx9Ware()
    :members:

Electron
~~~~~~~

.. attributetable:: Electron

.. autoclass:: weao.exploit.Electron()
    :members:

WeAreDevs
~~~~~~~

.. attributetable:: WeAreDevs

.. autoclass:: weao.exploit.WeAreDevs()
    :members:

OxygenU
~~~~~~~

.. attributetable:: OxygenU

.. autoclass:: weao.exploit.OxygenU()
    :members:

Fluxus
~~~~~~~

.. attributetable:: Fluxus

.. autoclass:: weao.exploit.Fluxus()
    :members:

Celestial
~~~~~~~

.. attributetable:: Celestial

.. autoclass:: weao.exploit.Celestial()
    :members:

Comet
~~~~~~~

.. attributetable:: Comet

.. autoclass:: weao.exploit.Comet()
    :members:


Hydrogen
~~~~~~~

.. attributetable:: Hydrogen

.. autoclass:: weao.exploit.Hydrogen()
    :members:

Exceptions
----------

.. autoexception:: WEAOException()

.. autoexception:: UnsupportedExploit()

.. autoexception:: StatusUnavailable()

.. autoexception:: LogsUnavailable()

.. autoexception:: ExploitNotFound()


Exception Hierarchy
~~~~~~~~~~~~~~~~~~~~~

.. exception_hierarchy::

    - :exc:`Exception`
        - :exc:`WEAOException`
           - :exc: `HTTPException`
            - :exc:`NotFound`
            - :exc:`WEAOUnavailable`
