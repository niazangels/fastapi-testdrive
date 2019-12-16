from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Sup, bro?"}


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
