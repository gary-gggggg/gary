from django.db import models
from topic.models import Topic
from user.models import UserProfile


# Create your models here.
class Message(models.Model):
    content = models.CharField('内容', max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)
    parent_message = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
