import time
from functools import wraps


# -------------------------
# 1. TIMER DECORATOR
# -------------------------

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Time taken: {end - start:.5f} seconds")

        return result

    return wrapper


# -------------------------
# 2. RETRY DECORATOR
# -------------------------

def retry(n, delay):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(1, n + 1):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    print(f"Attempt {attempt} failed: {e}")

                    if attempt == n:
                        raise

                    time.sleep(delay)

        return wrapper

    return decorator


# -------------------------
# 3. MEMOIZE DECORATOR
# -------------------------

def memoize(func):

    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):

        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            print("Returning cached result")
            return cache[key]

        result = func(*args, **kwargs)

        cache[key] = result

        return result

    return wrapper


# -------------------------
# TEST TIMER
# -------------------------

@timer
def add(a, b):

    time.sleep(1)

    return a + b


print("Addition:", add(10, 20))


# -------------------------
# TEST RETRY
# -------------------------

attempts = 0


@retry(3, 1)
def unstable_function():

    global attempts

    attempts += 1

    if attempts < 3:
        raise ValueError("Something went wrong")

    return "Success!"


print(unstable_function())


# -------------------------
# TEST MEMOIZE
# -------------------------

@memoize
def square(n):

    print("Calculating square...")

    return n * n


print(square(5))
print(square(5))
print(square(6))


# -------------------------
# TEST WRAPS
# -------------------------

print(add.__name__)
print(unstable_function.__name__)
print(square.__name__)