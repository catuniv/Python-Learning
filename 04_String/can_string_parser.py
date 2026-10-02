data = input("CAN Data: ")
data = data.strip()

speed, rpm, status = data.split(",")
speed = int(speed)
rpm = int(rpm)

print("=== CAN DATA ===")
print(f"Speed: {speed} km/h")
print(f"RPM: {rpm}")
print(f"Status: {status.upper()}")
