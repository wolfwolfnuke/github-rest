from fastapi import FastAPI
import uvicorn
import discord
import asyncio
import threading
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

app = FastAPI()
@app.get("/hello")
def hello():
    return {"message": "Hello, RaspAPI!"}
@app.get("/double")
def double(x: int):
    return {"result": x * 2}
@app.get("/send")
async def send(m:str,c:int):
    channel = client.get_channel(c)
    if channel is None:
        channel = await client.fetch_channel(c)
    await channel.send("m")
    return {"status": "sent"}

token = os.environ['DISCORDTOKEN']
t1 = threading.Thread(target=lambda: client.run(token))
t2 = threading.Thread(target=lambda: uvicorn.run(app))

async def main():
    discord_async_task = asyncio.create_task(client.start(token))
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, loop="asyncio")
    server = uvicorn.Server(config)
    uvicorn_task = asyncio.create_task(server.serve())
    await asyncio.gather(discord_async_task,uvicorn_task)


asyncio.run(main())
'''
uvicorn.run(app)
print("starting discord thread")
t1.start()
print("started discord thread")
print("starting uvicorn thread")
t2.start()
print("started uvicorn thread")
t1.join()
t2.join()
'''
