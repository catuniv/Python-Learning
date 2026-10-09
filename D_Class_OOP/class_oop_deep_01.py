class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class ElectricVehicle(Vehicle):
    def __init__(self, name, speed, battery):
        super().__init__(name, speed)
        self.battery = battery

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Speed: {self.speed}")
        print(f"Battery: {self.battery}")


ev = ElectricVehicle("Ioniq", 120, 85)
ev.show_info()
