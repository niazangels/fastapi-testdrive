from fastapi import FastAPI
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Sup, bro?"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


# Because path operations are evaluated in order, you need to make sure
# that the path for /users/me is declared before the one
# for /users/{user_id}:app.get("/user/me")
@app.get("/user/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        description = "Alex Krizhevsky would be proud"
    elif model_name == ModelName.resnet:
        description = "We have a Kaiming He fanboy!"
    else:
        description = "Yann LeCunn all the way."
    return {"model": model_name, "description": description}
