from django.db import models
import uuid
# Create your models here.
class Student(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    city = models.CharField(max_length=100)
    def __str__(self):
        return self.name
