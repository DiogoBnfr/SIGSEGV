from mongoengine import Document, StringField, DateTimeField

class Article(Document):
    title = StringField(required=True)
    author = StringField(required=True)
    content = StringField(required=True)
    date = DateTimeField(auto_now_add=True)
