from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
  title = models.CharField(max_length=255)
  completed = models.BooleanField(default=False)
  
  def __str__(self):
    return self.title
