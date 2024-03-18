import asyncio
import json
import numpy as np
import neurokit2 as nk
import websockets

ecg_12 = nk.ecg_simulate(duration = 100, method = "multileads")
print(ecg_12)

# print(ecg_12)
async def ws_server(websocket):
    print('Websocket server started')
    try:
        while True:
            ## COMMENT: You should send a line of the dataframe as a string. Use json for this too.
            await websocket.send(ecg_12)
    except websocket.ConnectionClosedError:
        print('Internal server error')

async def main():
    async with websockets.serve(ws_server,"localhost",7890):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
