# Question 1
print()
print("Question 1")
import numpy as np
data = np.array([60, 80, 100, 120, 140, 160])

print(data[0])
print(data[-1])
print(data[2:5])
print(data[0::2])
print(data[::-1])



# Question 2
print()
print("Question 2")
sensor = np.array([
    [80, 2000],
    [100, 2500],
    [120, 3000],
    [140, 3500]
])

print(sensor[0])
print(sensor[2][1])
print(sensor[:,0])
print(sensor[:,1])
print(sensor[1:])

# Question 3
print()
print("Question 3")
matrix = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print(matrix[0, 1:3])
print(matrix[1:3, 1])
print(matrix[1:3, 2:4])

