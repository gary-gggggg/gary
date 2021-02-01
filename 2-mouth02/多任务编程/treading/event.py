from multiprocessing import Event
e=Event()
print(e.is_set())
e.wait()
