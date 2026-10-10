log = "0x100,120,2500"

can_id, speed, rpm = log.split(",")

speed = int(speed)
rpm = int(rpm)

print("=== CAN DATA ===")
print(f"ID: {can_id}")
print(f"Speed: {speed}")
print(f"RPM: {rpm}")


