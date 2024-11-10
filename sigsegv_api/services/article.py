from fastapi import APIRouter, Depends, HTTPException
from models import Article, User
from schemas import ArticleSchema


class ArticleView:
    router = APIRouter(tags=["Articles"], prefix="/article")

    @router.get("/all")
    async def list_blogs() -> list[dict]: 

        articles : Article= Article.objects()

        output_articles : list[dict] = []

        for article in articles:
            dump_article : dict = {}
            dump_article["title"] = article.title
            dump_article["content"] = article.content
            dump_article["author_id"] = str(article.author_id)

            output_articles.append(dump_article)
                    
        return output_articles
    

    @router.get("")
    async def get_blog(article_id : str) -> dict: 

        article: Article = Article.objects(id=article_id).first()

        return {"New_tile": article.title, "New_content": article.content}


    @router.post("")
    async def post_article(article_data: ArticleSchema):

        try:
            user : User = User.objects(id=article_data.author_id).first()
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid author ID format")
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        new_article : Article = Article()
        new_article.title = article_data.title
        new_article.author_id = user.id
        new_article.content = article_data.content

        new_article.save()

        user.update(push__articles_id=new_article.id)

        return {"message": "Creating a new blog"}
    
    
    @router.put("")
    async def update_article(article_id : str, article_data : ArticleSchema) -> dict | None:

        article: Article = Article.objects(id=article_id).first()

        article.title = article_data.title
        article.content = article_data.content

        #TODO fazer uma funçao para fazer update
        article.update(
            set__title=article_data.title,
            set__content=article_data.content
        ) 

        return {"New_tile": article.title, "New_content": article.content}
    
    @router.delete("")
    async def delete_article(article_id : str) -> str:
        article: Article = Article.objects(id=article_id).first()

    #TODO fazer uma funçao para fazer delete
        article.delete()

        return "Artigo apagado com sucesso."



article_router = ArticleView.router