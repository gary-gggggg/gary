from django.db import models


# Create your models here.
class Content(models.Model):
    desc = models.CharField(max_length=50)
    # upload_to的值为media下的子目录，文件上传后放到该子目录下
    myfile = models.FileField(upload_to='myfiles')
