from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str 
    email: str
    articles_id: str | None = None
    comments_id: str | None = None

    class Config:
        orm_mode = True