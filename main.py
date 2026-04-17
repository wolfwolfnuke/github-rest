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
token = os.environ['DISCORDTOKEN']
t1 = threading.Thread(target=lambda: client.run(token))
t2 = threading.Thread(target=lambda: uvicorn.run(app))
#uvicorn.run(app)
print("starting discord thread")
t1.start()
print("started discord thread")
print("starting uvicorn thread")
t2.start()
print("started uvicorn thread")
t1.join()
t2.join()

