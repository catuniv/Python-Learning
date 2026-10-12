import numpy as np
# Question 1
print("Question 1")

speed = np.array([60, 80, 100, 120])
print(speed + 10)
print(speed * 2)
print(speed / 10)





# Question 2
print()
print("Question 2")

a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

print(a + b)
print(a - b)
print(a * b)
print(a / b)



# Question 3
print()
print("Question 3")

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

add = np.array([1, 2, 3])
result = data.copy()
result[:,0] = result[:,0] + 100

print(f"{data + add}\n")
print(f"{data * 2}\n")
print(result)
