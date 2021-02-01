from celery import Celery
import time
# 1 创建celery对象
app = Celery('giao2', broker='redis://@127.0.0.1:6379/1',
             backend='redis://@127.0.0.1:6379/2',)

@app.task
def  task_test(a,b):
    print('task is running')
    time.sleep(3)
    return a+b