import aiohttp
import pytest

from weao.client import Client


@pytest.mark.asyncio
async def test_get_status() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    status = await client.get_status()
    await client.cleanup()

    assert status.synapse.website == "https://x.synapse.to"


@pytest.mark.asyncio
async def test_get_roblox() -> None:
    session = aiohttp.ClientSession()
    client = Client(session=session)

    roblox = await client.get_roblox()
    await client.cleanup()

    assert roblox.windows.player == "WindowsPlayer"
