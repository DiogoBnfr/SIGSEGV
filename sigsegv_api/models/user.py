from mongoengine import Document, ListField, StringField, EmailField, ObjectIdField

class User(Document):
    username = StringField(max_length=50, required=True, unique=True)
    email = EmailField(max_length=50, required=True, unique=True)
    articles_id = ListField(ObjectIdField(), required=False)
    comments_id = ListField(ObjectIdField(), required=False)
