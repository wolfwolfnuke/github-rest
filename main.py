
from fastapi import FastAPI
import uvicorn
import discord
import asyncio
import threading

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

#t1 = threading.Thread(target=client.run())
t2 = threading.Thread(target=uvicorn.run(app))
#uvicorn.run(app)
print("starting uvicornthread")
t2.start()
print("started uvicorn thread")
t2.join()
