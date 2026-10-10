logs = [
    "0x100,80,2500",
    "0x200,120,3200",
    "0x100,90,2700",
    "0x300,70,2100",
    "0x200,130,3300"
]

print("=== HIGH SPEED LOG ===")
count = {}

for log in logs:
    can_id, speed, rpm = log.split(",")
    speed = int(speed)
    rpm = int(rpm)

    count[can_id] = count.get(can_id, 0) + 1

    if speed >= 120:
        print(f"{can_id} {speed} {rpm}")


print()

print("=== COUNT ===")
for can_id, value in count.items():
    print(f"{can_id}: {value}")
    

