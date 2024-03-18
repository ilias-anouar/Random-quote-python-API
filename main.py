from typing import Annotated, Union
import uvicorn
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import json
import random

range = {"start": 0, "end": 350}

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# V1
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


# V2
@app.get("/api/v2/quotes/{option}")
def read_random(
    option: str,
    author: Union[str, None] = None,
    date: Union[str, None] = None,
    keyword: Union[str, None] = None,
    id: Union[int, None] = None,
):
    f = open("./data/quotes.json")
    data = json.load(f)
    if option == "random":
        f.close()
        return [data[random.randrange(range["start"], range["end"])]]
    elif option == "search":
        if author != None:
            print(f"this is author : {author}")
            f.close()
            result = []
            for i in data:
                if i["author"].find(author) > -1:
                    result.append(i)
            if len(result) == 0:
                return {"Result": "There is no quote for this author"}
            else:
                return result
        elif date != None:
            print(f"this is date : {date}")
            f.close()
            result = []
            for i in data:
                if i["date"].find(date) > -1:
                    result.append(i)
            if len(result) == 0:
                return {"Result": "There is no quote in this date"}
            else:
                return result
        elif keyword != None:
            print(f"this is keyword : {keyword}")
            f.close()
            result = []
            for i in data:
                if i["quote"].find(keyword) > -1:
                    result.append(i)
            if len(result) == 0:
                return {"Result": "There is no quote with this keyword"}
            else:
                return result
        else:
            f.close()
            return {"Error": "Invalid Request"}
    elif option == "get":
        if id != None and id <= range["end"]:
            f.close()
            return [data[id]]
        else:
            f.close()
            return {"Error": "No quote with this ID"}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8200)
