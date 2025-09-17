from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "Hello, World!"}


@app.get("/about")
def hello_world():
    return {"this is ishuman!!"}
