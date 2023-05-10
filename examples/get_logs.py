import asyncio

from weao.client import Client


async def get_user() -> None:
    client = Client()

    logs = await client.get_logs("Synapse", 1)
    # [!] amount kwarg starts at 1 but python indexes from 0 don't forget that :P
    print(logs[0].last_update)
    print(logs[0].roblox_version)
    print(logs[0].version)
    await client.cleanup()


loop = asyncio.new_event_loop()
loop.run_until_complete(get_user())
