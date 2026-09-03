class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


# Example
numbers = CountUp(1, 5)

for number in numbers:
    print(number)