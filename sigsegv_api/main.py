from fastapi import FastAPI
from mongoengine import connect
from services import article_router, user_router

connect('sigsegvdb')

app = FastAPI()

app.include_router(article_router)
app.include_router(user_router)

@app.get("/home")
def index():
    return {"message": "Hello, world!"}
