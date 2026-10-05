sensor_data = [
        [80, 2500],
        [95, 2800],
        [110, 3100],
        [70, 2100],
        [130, 3500]
]

high_speed = []

print("=== HIGH SPEED DATA ===")

for speed, rpm in sensor_data:
    if speed >= 100:
        high_speed.append(speed)
        print(f"Speed: {speed}, RPM: {rpm}")

avg = sum(high_speed) / len(high_speed)

print(f"\nHigh Speed List: {high_speed}")
print(f"Average High Speed: {avg:.2f}")


