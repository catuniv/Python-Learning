import copy

sensor_data = [
        [80, 2500],
        [90, 2700],
        [120, 3200],
        [70, 2200]
]

count = 0
total = 0


print("=== SENSOR DATA ===")
for speed, rpm in sensor_data:
    print(f"Speed: {speed}, RPM: {rpm}") 
    total += speed
    if speed >= 100:
        count += 1
    

print()

print(f"High Speed Count: {count}")
print(f"Average Speed: {total / len(sensor_data):.2f}")
