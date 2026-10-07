vehicles = {
        "car1": {
            "speed":80,
            "rpm": 2500
        },
        "car2": {
            "speed":120,
            "rpm":3200
        },
        "car3": {
            "speed":60,
            "rpm":2100
        }
}

print("=== VEHICLE STATUS ===")

for car_name, car_info in vehicles.items():
    print(f"Car: {car_name}")
    print(f"Speed: {car_info["speed"]}")
    print(f"RPM: {car_info["rpm"]}")

    if car_info["speed"] >= 100:
        print("Status: HIGH SPEED\n")
    else:
        print("Status: NORMAL\n")
