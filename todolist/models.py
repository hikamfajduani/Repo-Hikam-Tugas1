from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class IsiTodolist(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    todo_date = models.TextField()
    todo_title = models.TextField()
    todo_description = models.TextField()
    is_finished = models.BooleanField(default=False)