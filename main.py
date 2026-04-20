from fastapi import FastAPI, HTTPException
import uvicorn
import discord
import asyncio
import threading
import os
import sqlite3
my_db = sqlite3.connect("api.db")
db_cursor = my_db.cursor()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

app = FastAPI()
@app.get("/send")
async def send(m:str,c:int,a:str):
    try:
        channel = client.get_channel(c)
        if channel is None:
            channel = await client.fetch_channel(c)
        await channel.send(m)
        succeded = "true"
        return {"status": succeded}

    except discord.errors.NotFound:
        raise HTTPException(404, "Channel not found. Did you put the channel name instead?")

    except discord.errors.Forbidden:
        raise HTTPException(403, "No permission to send messages. Is the bot in the server, and does it have permission to access and send messages in the channel?")

    

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
