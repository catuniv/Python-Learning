
speeds = [60, 80, 90, 130]

result = any(car_speed >= 120 for car_speed in speeds)
print(result)

result = all(car_speed >= 50 for car_speed in speeds)
print(result)
