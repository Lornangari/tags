

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
 title = models.CharField(max_length=255)
 author = models.ForeignKey(User, on_delete=models.CASCADE)
 text = models.TextField()
 created_date = models.DateTimeField(auto_now_add=True)
 published_date = models.DateTimeField(blank=True, null=True)

 def __str__(self):
  return self.title


class Editor(models.Model):
 first_name = models.CharField(max_length=100)
 last_name = models.CharField(max_length=100)
 email = models.EmailField()
 blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='editors')

def __str__(self):
 return f"{self.first_name} {self.last_name}"