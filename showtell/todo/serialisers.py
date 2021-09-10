from .models import TodoModel
# from rest_framework.serializers import Serializer, CharField, DateTimeField
from rest_framework.serializers import Serializer, CharField, DateTimeField

class TodoSerializer(Serializer):
    class Meta:
       model = TodoModel
       fields="__all__" 
    
    id = CharField(read_only=True, required=False)
    title = CharField()
    date = DateTimeField()
    description = CharField()
    
    def create(self, validated_data: dict) -> TodoModel:
        todo = TodoModel(**validated_data)
        todo.save()
        return todo
    
    def update(self, instance: TodoModel, validated_data: dict) -> TodoModel:
        instance.title = validated_data.get("title",instance.title)
        instance.description = validated_data.get("description",instance.description)
        instance.date = validated_data.get("date",instance.date)
        instance.save()
        return instance