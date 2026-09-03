from collections import deque

def task(name, steps):
    for i in range(steps):
        print(f"{name}: step {i + 1}")
        yield

class ToyEventLoop:
    def __init__(self):
        # Queue containing all tasks waiting to run
        self.tasks = deque()

    def create_task(self, coroutine):
        self.tasks.append(coroutine)

    def run(self):
        print("Event loop started\n")

        while self.tasks:
            current_task = self.tasks.popleft()

            try:
                next(current_task)
                self.tasks.append(current_task)

            except StopIteration:
                print("Task finished\n")

        print("Event loop finished")

loop = ToyEventLoop()

loop.create_task(task("Task A", 3))
loop.create_task(task("Task B", 3))
loop.create_task(task("Task C", 3))

loop.run()