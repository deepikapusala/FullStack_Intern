import copy
def show_copy_difference():

    original = [[1, 2], [3, 4]]

    # Shallow copy
    shallow = copy.copy(original)

    # Deep copy
    deep = copy.deepcopy(original)

    # Change a nested list
    shallow[0].append(99)
    deep[1].append(100)

    print("Original:", original)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)


show_copy_difference()