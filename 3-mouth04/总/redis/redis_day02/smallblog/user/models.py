from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    