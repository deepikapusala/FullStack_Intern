def fibonacci(n):
    a = 0
    b = 1

    for _ in range(n):
        yield a

        a, b = b, a + b


# Example
for number in fibonacci(10):
    print(number)