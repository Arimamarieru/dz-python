class Transport:
    def __init__(self, name: str, max_speed: int, mileage: int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return (f"Название автомобиля: {self.name} "
                f"Скорость: {self.max_speed} "
                f"Пробег: {self.mileage}")

    def seating_capacity(self, capacity: int) -> str:
        return (f"Вместимость одного автобуса {self.name}: "
                f"{capacity} пассажиров")


class Autobus(Transport):

    def seating_capacity(self, capacity: int = 50) -> str:
        
        return super().seating_capacity(capacity)



if __name__ == "__main__":
 
    bus = Autobus("Renaul Logan", 180, 12)
    print(bus)                           

    print(bus.seating_capacity())       
