from typing import Union
import uvicorn
from fastapi import FastAPI
import json
import random

range = {"start": 0, "end": 350}

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/quotes/{option}")
def read_random(option: str, id: Union[int, None] = None):
    f = open("./data/quotes.json")
    data = json.load(f)
    if option == "random":
        f.close()
        return [data[random.randrange(range["start"], range["end"])]]
    elif option == "get":
        if id != None and id <= range["end"]:
            f.close()
            return [data[id]]
        else:
            f.close()
            return {"Error": "the quote's id not defined"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8200)
