# command palette + REPL = interactive mode
##disadvantage: nothing is saved! (think the ide from python 1)
import numpy as np

"""
# List Comprehension
# Create a one-dimensional array from a list
# that produces even integers from 2 through 20

integers = np.array([x for x in range(2, 21, 2)])
print(integers)

integers = np.array([[1, 2, 3], [4, 5, 6]])
print(integers)

floats = np.array([0.0, 0.1, 0.2, 0.3])
print(floats)

a = integers.dtype
b = integers.ndim
c = integers.shape  # number rows and number of columns
d = integers.size

print()

for row in integers:
    print(type(row))
    print(row)
    for col in row:
        print(col)

for i in integers.flat:
    print(i)
"""

##########################
##EXERCISE##
##########################

# create a 2-dimensional array of 5 integer elements(1-10) each using the random module
# and list comprehension print out its dimension, shape, and size


import random

"""
myarray = np.array(
    [
        [random.randint(1, 10) for i in range(5)],
        [random.randint(1, 10) for i in range(5)],
    ]
)
print(myarray)

b = np.array(np.random.randint(1, 10, size=(2, 5)))
print(b)

c = np.zeros(5)  # create array of 5 elements of seroes
print(np.ones(5))  # create an array of 5 elements of 1s
print(np.ones((2, 4), dtype=int))  # create an array of 2 by 4 of ones of type int

print(np.full((3, 5), 13))  # produces an arrange of size 3 X 5 of #13

print(np.arange(5, 10))  # includes lower limit but not upper limit

print(np.arange(10, 1, -2))  # step value for descending order

# Linespace: allows us to give it two numbers and it will create an array
##between 0.0 and 1.0
###Float; evenly spaced

print(np.linspace(0.0, 1.0, num=5))
# Useful when studying math or huge arrays of numbers
"""
"""
array1 = np.arange(1, 21)
array2 = array1.reshape(4, 5)  # divides 1 into 4 rows and 5 columns

print(array1)
print(array2)

array3 = np.arange(1, 100001).reshape(4, 25000)

print(array3)

array4 = np.arange(1, 100001).reshape(100, 1000)
print(array4)
"""
# Augemented assignemnts?

numbers = np.arange(1, 6)

numbers += 10

print(numbers)

# broadcasting
print(numbers * 2)

print(numbers ** 3)

# Shockingly enouhg, there are no permanent changes to numbers
print(numbers)

numbers2 = np.linspace(1.1, 5.5, 5)
a = numbers * numbers2
print(a)

# Comparing arrays

print(numbers >= 13)

print(numbers2 < numbers)

print(numbers == numbers2)
