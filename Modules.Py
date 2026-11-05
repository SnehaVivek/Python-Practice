# Modules in Python
import math
import random
import datetime

# Using the math module to perform various mathematical operations.
print(math.sqrt(100))
print(math.factorial(5))
print(math.ceil(10.3))
print(math.floor(10.3))
print(math.pow(2,3))
print(math.pi)

# Round function rounds a number to the nearest integer.
print(round(11.3))
print(round(11.7))

# Using the random module to generate a random integer between 1 and 100.
print(random.randint(1, 100))

# Using the random module to select a random student from a list and shuffle the list of students.
students = ["Amit", "Rahul", "Priya", "Neha"]
print(random.choice(students))
random.shuffle(students)
print(students)

# Using the datetime model to get the current date and time.
print(datetime.date.today())
print(datetime.datetime.now())