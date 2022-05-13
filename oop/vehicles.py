class Vehicle:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def move(self, x):
        print(f'Moving {self.manufacturer} by {x} meters')


class VehicleWithEngine(Vehicle):
    def __init__(self, manufacturer, engine_size, fuel):
        super().__init__(manufacturer)
        self.engine_size = engine_size
        self.fuel = fuel

    def tank(self, x):
        print(f'{self.manufacturer}: tanking {x} liters of {self.fuel}')

    def carry(self):
        raise NotImplementedError


class Car(VehicleWithEngine):
    def __init__(self, manufacturer, engine_size, fuel, no_of_passengers, no_of_doors):
        super().__init__(manufacturer, engine_size, fuel)
        self.passengers = no_of_passengers
        self.doors = no_of_doors

    def carry(self):
        print(f'{self.manufacturer}: can carry up to {self.passengers} people, who can enter with {self.doors} doors')


class Motorcycle(VehicleWithEngine):
    def carry(self):
        print(f'{self.manufacturer}: can carry up to 2 people who sit on top of a motorcycle.')


class Bicycle(Vehicle):
    pass