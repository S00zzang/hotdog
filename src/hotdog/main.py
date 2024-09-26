from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Welcome to HOTDOG WORLD"}
