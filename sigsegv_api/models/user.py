from mongoengine import Document, EmailField, StringField, ListField, LazyReferenceField

class User(Document):
    username = StringField(max_lenght=50, required=True, unique=True)
    email = EmailField(max_lenght=50, required=True, unique=True)
    articles = ListField(LazyReferenceField('Article'))
    comments = ListField(LazyReferenceField('Comment'))
