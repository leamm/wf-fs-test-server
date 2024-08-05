import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/items")
async def root():
    with open("items.json", "r") as file:
        items = json.load(file)
    return items
