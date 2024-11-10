from mongoengine import Document, ListField, StringField, DateTimeField, ObjectIdField

class Article(Document):
    title = StringField(max_length=100, required=True)
    author_id = ObjectIdField(required=True)
    content = StringField(required=True)
    date = DateTimeField(auto_now_add=True)
    comments_id = ListField(ObjectIdField())