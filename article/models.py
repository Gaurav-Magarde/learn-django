from django.db import models
import uuid
# Create your models here.

class Article(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000,null=True,blank=True)
    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title