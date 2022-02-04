import threading
import time


def threads_count():
    num = threading.active_count()
    # return num
    print(f'Running threads: {num}')

def sleep():
    start = time.time()
    time.sleep(3)
    print(f'time = {time.time() - start} seconds')

threads_count()
sleep()
t1 = threading.Thread(target=threads_count)

t2 = threading.Thread(target=sleep)

t1.start()
t2.start()








