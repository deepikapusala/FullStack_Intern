# def create_counter():

#     count = 0

#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return counter


# counter = create_counter()

# print(counter())
# print(counter())
# print(counter())

def create_counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    def get_count():
        return count

    return increment, get_count


increment, get_count = create_counter()

print(increment())
print(increment())
print(get_count())