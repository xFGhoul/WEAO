import asyncio

from weao.client import Client


async def get_user() -> None:
    client = Client()

    status = await client.get_status()
    print(status.synapse.updated)
    print(status.script_ware.updated)
    print(status.krnl.updated)
    # [!] has all other exploits, just listed 3...
    await client.cleanup()


loop = asyncio.new_event_loop()
loop.run_until_complete(get_user())
