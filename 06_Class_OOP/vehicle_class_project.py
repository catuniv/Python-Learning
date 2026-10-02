class Vehicle:
    def __init__ (self, name, speed, rpm):
        self.name = name
        self.speed = speed
        self.rpm = rpm

    def show_info(self):
        print(f"Vehicle : {self.name}")
        print(f"Speed : {self.speed}")
        print(f"Rpm : {self.rpm}")

    def set_speed(self, newSpeed):
        self.speed = newSpeed

    def status(self):
        if self.speed >= 80:
            print("FAST")
        elif self.speed >= 40:
            print("NORMAL")
        else:
            print("SLOW")


car = Vehicle("Avante", 60, 2500)
car.set_speed(120)
car.show_info()
car.status()


