from fastapi import APIRouter, Depends
from models import User
from schemas import UserSchema

class UserView:
    router = APIRouter(tags=["users"], prefix="/user")

    @router.get("/")
    async def list_blogs() -> list[UserSchema]:
        
        return {"message": "Listing all users"}

    @router.post("/")
    async def post_article(user_data: UserSchema):

        new_user = User()

        new_user.username = user_data.username
        new_user.email = user_data.email

        new_user.save()

        return {"message": f"Creating a new user id: {new_user.id}"}

user_router = UserView.router