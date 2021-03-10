import numpy as np

"""
grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

# ROWS = grades for each student
# COLS = grades for each test

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis=0)
print("Average of each test:", g)

h = grades.mean(axis=1)
print("Average of each student:", h)

# By specifying access, we can determine how we want these to be printed out/calculated
##Axis[0] calculates the mean based on the test! [0] is by column for every row
##Axis[1] calculates by ROW, which is for each student

numbers = np.array([1, 4, 9, 16, 25, 36])

sqrt = np.sqrt(numbers)
print(sqrt)

numbers2 = np.arange(1, 7) * 10
add = np.add(numbers, numbers2)

print(add)

multiply = np.multiply(numbers2, 5)

print(multiply)


numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

multiply2 = np.multiply(numbers3, numbers4)

print(multiply2)

"""
# indexing and slicing

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])

b = grades[1]
# array ([100,87,90])

# firsttwo = grades[0:2]
# array([[87,96,70],[100,87,90]])

c = grades[:2, 0]

# print(c)

# [ 87 100  94 100]

# [:2,0] = [87,100]


d = grades[:, 1:3]
# print(d)
# Array : [ 87 100]
# [[96 70]  #Getting the second and third element
# [87 90]
# [77 90]
# [81 82]]

e = grades[:, [0, 2]]
# print(e)
"""array: [[ 87  70]
 [100  90]
 [ 94  90]
 [100  82]]"""

# Consecutive uses colons; nonconsecutive uses commas


# EXERCISE:
random_grades = np.array(np.random.randint(60, 100, size=(3, 4)))
# OR: grades = np.random.randint(60,100,12).reshape(3,4)
print(random_grades)

grades_means = random_grades.mean(axis=0)

grades_student_means = random_grades.mean(axis=1)

print(grades_means)
print(grades_student_means)