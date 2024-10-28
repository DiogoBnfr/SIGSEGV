from mongoengine import LazyReferenceField, Document, StringField, DateTimeField

class Comment(Document):
    content = StringField(max_length=200,required=True)
    date = DateTimeField(auto_now_add=True)
    author = LazyReferenceField('User', required=True, reverse_delete_rule=CASCADE)
    article = LazyReferenceField('Article', required=True, reverse_delete_rule=CASCADE)
