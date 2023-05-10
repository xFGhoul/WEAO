import asyncio
import aiohttp

from weao.client import Client


async def get_user() -> None:
    session = aiohttp.ClientSession()

    client = Client(session=session, use_alternative_api=True)
    # [!] you may also define your own aiohttp session
    # [!] as well as defining whether you want to use the alternative api url compared to the main one
    synapse = await client.get_exploit("Synapse")
    # [!] exploit arg MUST be a valid name, the list is in constants.py
    print(synapse.is_free)
    print(synapse.last_update)
    print(synapse.website)
    await client.cleanup()
    # [!] Please do not forget to cleanup!


loop = asyncio.new_event_loop()
loop.run_until_complete(get_user())
