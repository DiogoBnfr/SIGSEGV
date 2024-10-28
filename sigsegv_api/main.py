from fastapi import FastAPI
from mongoengine import connect

connect('sigsegvdb')

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, world!"}
