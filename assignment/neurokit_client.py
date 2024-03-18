import websockets
import asyncio

async def ws_client():
    print('Websockets: Client Connected')
    url = "ws://localhost:7890"

    async with websockets.connect(url) as ws:
        while True:
            msg = await ws.recv()
            print(msg)
asyncio.run(ws_client())