from pydantic import BaseModel

class ArticleSchema(BaseModel):
    title: str
    author_id: str
    content: str

    class Config:
        orm_mode = True