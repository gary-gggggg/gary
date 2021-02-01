import redis

r = redis.Redis(password="123456")
try:
    while 1:
        task = r.brpop('giaolst', 5)
        print(task)
        if task:
            # 处理任务
            task_data = task[1]
            task_str = task_data.decode()
            task_list = task_str.split('_')
            print(f"receive task {task_list[0]}")
            if task_list[0] == 'sendMail':
                print('call send mail function')
            else:
                pass
        else:
            print('********no task********')
except KeyboardInterrupt as hh:
        print(hh)
