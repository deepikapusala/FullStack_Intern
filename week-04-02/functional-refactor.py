from functools import reduce, partial


students = [
    {"name": "Deepika", "marks": 85},
    {"name": "Koushik", "marks": 45},
    {"name": "Sneha", "marks": 72},
    {"name": "Rahul", "marks": 30},
    {"name": "Priya", "marks": 90}
]


# Check whether student passed
def is_passed(student):
    return student["marks"] >= 50


# Add bonus marks
def add_bonus(bonus, student):
    return {
        "name": student["name"],
        "marks": student["marks"] + bonus
    }


# Get marks
def get_marks(student):
    return student["marks"]


# Add two numbers
def add(a, b):
    return a + b


# 1. Filter passed students
passed_students = filter(is_passed, students)


# 2. Create function that always adds 5 bonus marks
add_five_bonus = partial(add_bonus, 5)


# 3. Add bonus to every passed student
students_with_bonus = map(add_five_bonus, passed_students)


# 4. Get only the marks
marks = map(get_marks, students_with_bonus)


# 5. Convert to list because map gives an iterator
marks = list(marks)


# 6. Calculate total
total = reduce(add, marks)


# 7. Calculate average
average = total / len(marks)


print("Marks:", marks)
print("Total:", total)
print("Average:", average)