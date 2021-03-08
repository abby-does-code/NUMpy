
import numpy as np

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

#ROWS = grades for each student
#COLS = grades for each test

a = grades.sum()
b = grades.min()
c = grades.max()
d = grades.mean()
e = grades.std()
f = grades.var()

g = grades.mean(axis = 0)
print("Average of each test:" g)

h = grades.mean(axis = 1)
print("Average of each student:" h)

#By specifying access, we can determine how we want these to be printed out/calculated
##Axis[0] calculates the mean based on the test! [0] is by column for every row
##Axis[1] calculates by ROW, which is for each student