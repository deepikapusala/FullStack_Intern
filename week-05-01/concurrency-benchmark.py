
import asyncio
import threading
import multiprocessing
import time


# ============================================================
# 1. I/O-BOUND TASK
# ============================================================
# Imagine this is a network call.
# We use sleep() to simulate waiting for a server response.


def io_task(task_number):
    time.sleep(1)
    return f"Task {task_number} finished"


# ---------------- THREADING ----------------

def run_io_threading(number_of_tasks):
    threads = []

    for i in range(number_of_tasks):
        thread = threading.Thread(
            target=io_task,
            args=(i,)
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


# ---------------- MULTIPROCESSING ----------------

def run_io_multiprocessing(number_of_tasks):
    with multiprocessing.Pool() as pool:
        pool.map(io_task, range(number_of_tasks))


# ---------------- ASYNCIO ----------------

async def async_io_task(task_number):
    # asyncio.sleep() does NOT block the event loop
    await asyncio.sleep(1)
    return f"Task {task_number} finished"


async def run_io_asyncio(number_of_tasks):
    tasks = []

    for i in range(number_of_tasks):
        tasks.append(async_io_task(i))

    await asyncio.gather(*tasks)


# ============================================================
# 2. CPU-BOUND TASK
# ============================================================
# This function does heavy mathematical work.
# There is no waiting here.


def cpu_task(number):
    total = 0

    for i in range(5_000_000):
        total += i * i

    return total


# ---------------- THREADING ----------------

def run_cpu_threading(number_of_tasks):
    threads = []

    for i in range(number_of_tasks):
        thread = threading.Thread(
            target=cpu_task,
            args=(i,)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# ---------------- MULTIPROCESSING ----------------

def run_cpu_multiprocessing(number_of_tasks):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_task, range(number_of_tasks))


# ---------------- ASYNCIO ----------------

async def async_cpu_task(number):
    # CPU work is still normal synchronous Python work.
    # asyncio cannot magically run it in parallel.
    return cpu_task(number)


async def run_cpu_asyncio(number_of_tasks):
    tasks = []

    for i in range(number_of_tasks):
        tasks.append(async_cpu_task(i))

    await asyncio.gather(*tasks)


# ============================================================
# BENCHMARK HELPER
# ============================================================

def benchmark(name, function):
    start = time.perf_counter()

    function()

    end = time.perf_counter()

    print(f"{name:<30} {end - start:.2f} seconds")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    number_of_tasks = 10

    print("=" * 60)
    print("I/O-BOUND TASK")
    print("=" * 60)

    benchmark(
        "Threading",
        lambda: run_io_threading(number_of_tasks)
    )

    benchmark(
        "Multiprocessing",
        lambda: run_io_multiprocessing(number_of_tasks)
    )

    benchmark(
        "Asyncio",
        lambda: asyncio.run(
            run_io_asyncio(number_of_tasks)
        )
    )


    print("\n" + "=" * 60)
    print("CPU-BOUND TASK")
    print("=" * 60)

    benchmark(
        "Threading",
        lambda: run_cpu_threading(number_of_tasks)
    )

    benchmark(
        "Multiprocessing",
        lambda: run_cpu_multiprocessing(number_of_tasks)
    )

    benchmark(
        "Asyncio",
        lambda: asyncio.run(
            run_cpu_asyncio(number_of_tasks)
        )
    )

