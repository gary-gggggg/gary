from celery import Celery
import time

# 1 初始化celery，指定broker:创建Celery对象
app = Celery('giao', broker='redis://@127.0.0.1:6379/1')


# 2创建任务函数
@app.task
def task_test():
    time.sleep(3)
    print('task is running....')
