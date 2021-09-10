from django.db.models import Model, CharField, DateTimeField, TextField, UUIDField
from uuid  import uuid4

class TodoModel(Model):
    id = UUIDField(primary_key=True,default=uuid4)
    title = CharField(max_length=255)
    date = DateTimeField()
    description = TextField()