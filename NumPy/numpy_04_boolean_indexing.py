# Question 1
print("Question 1")
import numpy as np
speed = np.array([60, 80, 100, 120, 140, 160])

print(speed[speed >= 100])
result = speed[(speed >= 80) & (speed <= 140)]
result2 = speed[(speed < 100) | (speed > 140)]

print(result)
print(result2)


print()
# Question 2
print("Question 2")
rpm = np.array([1500, 2000, 2500, 3000, 3500, 4000])
result3 = rpm[rpm >= 3000];
result4 = rpm[(rpm > 2000) & (rpm < 3500)]
result5 = rpm[(rpm <= 2500) | (rpm >= 4000)]
print(result3)
print(result4)
print(result5)


print()
# Question 3
print("Question 3")
sensor = np.array([
    [80, 2000],
    [100, 2500],
    [120, 3000],
    [140, 3500],
    [160, 4000]
])

result6 = sensor[sensor[:,0] >= 120]
result7 = sensor[sensor[:,1] >= 3000]
result8 = sensor[(sensor[:,0] >= 100) & (sensor[:,1] <= 3500)]

print(result6)
print()
print(result7)
print()
print(result8)
