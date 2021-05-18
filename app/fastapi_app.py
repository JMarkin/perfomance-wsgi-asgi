import time
import asyncio

from fastapi import FastAPI



app = FastAPI()


@app.get("/async-txt")
async def async_txt():
    await asyncio.sleep(1)
    return "Hello"


@app.get("/sync-txt")
def sync_txt():
    time.sleep(1)
    return "Hello"
