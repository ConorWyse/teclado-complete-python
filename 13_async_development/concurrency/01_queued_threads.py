import queue

from threading import Thread

counter = 0
job_queue = queue.Queue()       # items to print out
counter_queue = queue.Queue()   # amounts by which to increment `counter`


def increment_manager():
    global counter
    while True:
        increment = counter_queue.get()     # wait for item & lock the queue
        old_counter = counter
        counter = old_counter + increment
        job_queue.put((f'New counter value is {counter}', '-------'))
        counter_queue.task_done()           # release the lock


def printer_manager():
    while True:
        for line in job_queue.get():
            print(line)
        job_queue.task_done()


def increment_counter():
    counter_queue.put(1)


Thread(target=increment_manager, daemon=True).start()
Thread(target=printer_manager, daemon=True).start()

worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
    thread.start()

# Wait for the worker threads to finish *and* for the queues to become empty (not for the processes)
for thread in worker_threads:
    thread.join()

counter_queue.join()
job_queue.join()
