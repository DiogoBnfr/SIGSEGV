from mongoengine import LazyReferenceField, Document, StringField, DateTimeField

class Comment(Document):
    author = LazyReferenceField('User')
    content = StringField(max_length=200,required=True)
    date = DateTimeField(auto_now_add=True)
    article = LazyReferenceField('Article')
