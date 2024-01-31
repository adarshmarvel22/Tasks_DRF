from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'is_completed']  

class BulkTaskSerializer(serializers.Serializer):
    tasks = TaskSerializer(many=True)
