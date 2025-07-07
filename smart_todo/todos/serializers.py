from rest_framework import serializers
from .models import Task, ContextEntry
import json

class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['tags'] = instance.get_tags_list()
        return data

    def to_internal_value(self, data):
        tags = data.get('tags', [])
        data = super().to_internal_value(data)
        data['tags'] = json.dumps(tags)
        return data

class ContextEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextEntry
        fields = '__all__'
