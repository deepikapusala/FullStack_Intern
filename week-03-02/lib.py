import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print("Time taken:", end - start, "seconds")


with timer():
    total = 0
    for i in range(1000000):
        total += i