
def show_vehicle(**kwargs):
    print(f"Name: {kwargs["name"]}")
    print(f"Speed: {kwargs["speed"]}")
    print(f"RPM: {kwargs["rpm"]}")
    if kwargs["speed"] >= 100:
        print("HIGH")
    else:
        print("NORMAL")


show_vehicle(name="Avante", rpm=3200, speed=120)
