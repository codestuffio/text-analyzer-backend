from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_item(text: str):
    return {"message": text}
