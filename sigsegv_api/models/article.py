from mongoengine import Document, LazyReferenceField, StringField, DateTimeField

class Article(Document):
    title = StringField(max_length=100, required=True)
    author = LazyReferenceField('User', required=True, reverse_delete_rule=CASCADE)
    content = StringField(required=True)
    date = DateTimeField(auto_now_add=True)
