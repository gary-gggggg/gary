from celery import Celery
from django.conf import settings
import os

# 1 为celery设置环境变量，告知celery为哪一个django项目提供服务的
# os.environ.setdefault()
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'test_celery.settings')
# 2 创建应用
app = Celery('test_celery')

# 3 配置应用
app.conf.update(
    BROKER_URL='redis://@127.0.0.1:6379/1',
)

# 4 设置app自动发现和加载任务
app.autodiscover_tasks(settings.INSTALLED_APPS)
