class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.a = 0
        self.b = 1
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration

        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1

        return result

fib = Fibonacci(7)

for number in fib:
    print(number)
    