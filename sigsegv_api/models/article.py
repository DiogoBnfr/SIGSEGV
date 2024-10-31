from mongoengine import Document, LazyReferenceField, StringField, DateTimeField, CASCADE
from .user import User
from .comment import Comment

class Article(Document):
    title = StringField(max_length=100, required=True)
    author = LazyReferenceField('User', required=True, reverse_delete_rule=CASCADE)
    content = StringField(required=True)
    date = DateTimeField(auto_now_add=True)
    comment = LazyReferenceField('Comment')
