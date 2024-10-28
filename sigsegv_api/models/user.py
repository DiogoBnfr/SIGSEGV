from mongoengine import Document, StringField, ListField, LazyReferenceField

class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    article = ListField(LazyReferenceField('Article'))
    comments = ListField(LazyReferenceField('Comment'))
