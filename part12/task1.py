class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return (f"Название автомобиля: {self.name} "
                f"Скорость: {self.max_speed} "
                f"Пробег: {self.mileage}")

class Autobus(Transport):
    pass

bus = Autobus("Renaul Logan", 180, 12)
print(bus)                      
