# show and tell notes
```
cd projects/misc/python
poetry new aproj
cd aproj
poetry add django djangorestframework
poetry add --dev mypy black
code .
```
move over to ide
pop terminal
```
poetry shell
ctrl+shift+p type "python interpreter"
```
copy paste the path, remove "activate" and swap with "python" on the end
```
django-admin startproject myproj
cd myproj
ls
python manage.py migrate
python manage.py startapp todo
```
show folders, then open `myproj/settings.py` and add todo to installed_apps
open todo/models.py
```
from django.db.models import Model, CharField, TextField, DateTimeField, UUIDField
from uuid import uuid4


class TodoModel(Model):
    id = UUIDField(primary_key=True, default=uuid4)
    title = CharField(max_length=255)
    date = DateTimeField()
    description = TextField()

```
then in shell
```
./manage.py makemigrations
./manage.py migrate
```
create serialisers.py, then
```
from .models import TodoModel
from rest_framework.serializers import Serializer, CharField, DateTimeField


class TodoSerialiser(Serializer):
      class Meta:
        model = TodoModel
        fields = "__all__"

      id = CharField(read_only=False, required=False)
      title = CharField()
      date = DateTimeField()
      description = CharField()

      def create(self, validated_data: dict) -> TodoModel:
          todo = TodoModel(**validated_data)
          todo.save()
          return todo

      def update(self, instance: TodoModel, validated_data: dict) -> TodoModel:
          instance.title = validated_data.get("title", instance.title)
          instance.date = validated_data.get("date", instance.date)
          instance.description = validated_data.get("description", instance.description)
          instance.save()
          return instance

```
create api.py, then
```
from rest_framework.viewsets import ModelViewSet
from .serialisers import TodoSerialiser
from .models import TodoModel

class TodoViewSet(ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerialiser

```
then open myproj/urls.py and add
```
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.api import TodoViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'todo', TodoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]

```
then in console
```
./manage.py runserver
```
open postman and go over various payloads
