import asyncio
from aiohttp import web, ClientSession
from datetime import datetime
import json
#from getIP import getIP
from uAio import *
import subprocess
from cTransOpenAI import *

async def handle(request):
    with open("index.html", "r") as f:
        html_content = f.read()
    return web.Response(text=html_content, content_type='text/html')

async def handleControl(request):
    with open("control.html", "r") as f:
        html_content = f.read()
    return web.Response(text=html_content, content_type='text/html')

async def handlePost(request):
    data = await request.json()
    rData = {}
    print(data)
    # print(data["action"], data["value"])

    if data['action'] == "startRecording":     
        subprocess.run(['python3', 'every3.py'])

        rData['item'] = "startRecording"
        rData['status'] = "recording" # a string representing the current time

    if data['action'] == "getTranscript":     
        with open("AItext.txt", "r") as f:
            txt = f.read()

        rData['item'] = "getTranscript"
        rData['status'] = txt # a string representing the current time

    if data['action'] == "GetCustomSummary":     
        cTrans = customTranscript(data['value'])
        rData['item'] = "GetCustomSummary"
        rData['status'] = cTrans # a string representing the current time
    
    response = json.dumps(rData)
    print("Response: ", response)
    return web.Response(text=response, content_type='text/html')



# print "Hello" every 1 second (testing async)
async def print_hello():
    while True:
        print("Hello")
        await asyncio.sleep(1)

''' Get the light level from the MakerspaceNetwork Testing Pico'''
async def getLightLevel(dt=1):
    while True:
        await getRequest('20.1.0.96:80/photoResistor')
        # async with ClientSession() as session:
        #     async with session.get('http://20.1.0.96:80/photoResistor') as resp:
        #         print(resp.status)
        #         print(await resp.text())
        await asyncio.sleep(dt)


''' Get the dial value'''
async def getDialValue(ip="20.1.0.95:80"):
    try:
        D = await postRequest(ip,"dialPercent")
        print("dialValue:", D)
        return D
    except:
        print("could not get the dial percent")
  


async def main():
    app = web.Application()
   
    app.router.add_get('/', handle) 
    app.router.add_get('/control', handleControl)
    app.router.add_post("/", handlePost)

    runner = web.AppRunner(app)
    await runner.setup()

    host = getIP()
    site = web.TCPSite(runner, host, 8080)  # Bind to the local IP address
    await site.start()
    print(f"Server running at http://{host}:8080/")
    # await getDialValue()
    dialVal = await getDialValue() # asyncio.create_task(getDialValue())
    print("Dial Test:", dialVal)

#    asyncio.create_task(print_hello())
    asyncio.create_task(getLightLevel(dt=5))

    '''Testing post request'''
    # await postRequest("192.168.1.142:8000", action="Rhythmbox", value="play")
    # await postRequest("192.168.1.142:8000", action="Rhythmbox", value="play")

    await asyncio.Event().wait()  # Keep the event loop running

if __name__ == '__main__':
    asyncio.run(main())