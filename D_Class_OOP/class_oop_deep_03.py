class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self._speed = speed

    def set_speed(self, speed):
        if speed >= 0:
            self._speed = speed
        else:
            print("Invalid Speed")

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Speed: {self._speed}")


car = Vehicle("Avante", 80)

car.show_info()

car.set_speed(120)
car.show_info()


car.set_speed(-30)
car.show_info()
