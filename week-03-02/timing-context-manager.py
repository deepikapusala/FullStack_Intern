import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()

        self.elapsed = self.end - self.start

        print(f"Time taken: {self.elapsed:.4f} seconds")


# Example
with Timer():
    time.sleep(1)