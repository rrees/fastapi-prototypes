from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello world"}


@app.get("/greet/{name}")
async def greet(name: str):
    return {"message": f"Hello {name}"}
