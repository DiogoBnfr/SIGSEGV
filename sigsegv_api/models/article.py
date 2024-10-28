from mongoengine import Document, LazyReferenceField, StringField, DateTimeField

class Article(Document):
    title = StringField(max_lenght=100, required=True)
    author = LazyReferenceField('User', required=True)
    content = StringField(required=True)
    date = DateTimeField(auto_now_add=True)
