from fastapi import APIRouter, Depends, HTTPException
from models import Article, User
from pydantic import BaseModel


class ArticleSchema(BaseModel):
    title: str
    author_id: str
    content: str

    class Config:
        orm_mode = True


class ArticleView:
    router = APIRouter()

    @router.get("/")
    async def list_blogs(): 
        output_articles = Article.objects()

        return {"Artigos:": [{"title": article.title, "author": str(article.author.id), "content": article.content} for article in output_articles]}


    @router.post("/")
    async def post_article(article_data: ArticleSchema):
        user = User.objects(id=article_data.author_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        new_article = Article()
        new_article.title = article_data.title
        new_article.author = user
        new_article.content = article_data.content

        new_article.save(cascade=True)

        user.update(push__articles=new_article)

        return {"message": "Creating a new blog"}

article_router = ArticleView.router