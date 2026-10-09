class Vehicle:
    wheels = 4

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def __str__(self):
        return f"{self.name} - {self.speed} km/h - wheels: {self.wheels}"


car1 = Vehicle("Avante", 80)
car2 = Vehicle("Sonata", 100)

print(car1)
print(car2)


