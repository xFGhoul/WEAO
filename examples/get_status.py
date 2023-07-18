import asyncio

from weao.client import Client


async def get_status() -> None:
    client = Client()

    status = await client.get_status()
    print(status.synapse.website)
    print(status.script_ware.download_url)
    print(status.krnl.v3rmillion)
    # [!] has all other exploits, just listed 3...
    await client.cleanup()


loop = asyncio.new_event_loop()
loop.run_until_complete(get_status())
