import os
for i in os.listdir("/home/tarena/下载"):
    if os.path.getsize(f"/home/tarena/下载/{i}")<1024:
        os.remove(f"/home/tarena/下载/{i}")

