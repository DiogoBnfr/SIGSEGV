from mongoengine import Document, StringField, DateTimeField, ObjectIdField

class Comment(Document):
    content = StringField(max_length=200,required=True)
    date = DateTimeField(auto_now_add=True)
    author_id = ObjectIdField()
    articles_id = ObjectIdField()
