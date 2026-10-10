from collections import deque

logs = [
        "0x100,80,2500",
        "0x100,85,2500",
        "0x100,90,2600",
        "0x100,150,3200",
        "0x100,95,2700"
]

buffer = deque(maxlen=3)

for log in logs:
    can_id, speed, rpm = log.split(",")
    speed = int(speed)
    rpm = int(rpm)

    if buffer:
        avg = sum(buffer) / len(buffer)

        if abs(speed - avg) >= 40:
            print("ALERT")
        else:
            print("NORMAL")

    buffer.append(speed)
    print(buffer)
