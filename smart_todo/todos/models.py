from django.db import models
import json

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    priority = models.IntegerField(default=3)  # 1=High, 5=Low
    category = models.CharField(max_length=100, blank=True)
    tags = models.TextField(blank=True, default="[]")  # JSON list

    def get_tags_list(self):
        return json.loads(self.tags or "[]")

    def set_tags_list(self, tag_list):
        self.tags = json.dumps(tag_list)

class ContextEntry(models.Model):
    source = models.CharField(max_length=50)  # whatsapp, email
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
