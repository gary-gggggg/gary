from celery import Celery
import os
from django.conf import settings

# 1 告诉selery为哪个django服务
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ddblog.settings')

# 2 创建对象
app = Celery('ddblog')
# 3 配置celery
app.conf.update(
    BROKER_URL='redis://@127.0.0.1:6379/1'
)
# 告知celery 自动到django项目下去找任务函数
app.autodiscover_tasks(settings.INSTALLED_APPS)