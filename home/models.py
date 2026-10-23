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

class Project(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return self.title