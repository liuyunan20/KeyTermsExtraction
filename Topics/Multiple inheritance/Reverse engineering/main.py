# create the hierarchy here
class Vehicle:
    def __init__(self, name):
        self.type = 'Vehicle'
        self.name = name


class LandVehicle(Vehicle):
    def __init__(self, name):
        self.type = 'LandVehicle'
        self.name = name
        super().__init__(name)


class WaterVehicle(Vehicle):
    def __init__(self, name):
        self.type = 'WaterVehicle'
        self.name = name
        super().__init__(name)


class Car(LandVehicle):
    def __init__(self, name):
        self.type = 'Car'
        self.name = name
        super().__init__(name)


class Boat(WaterVehicle):
    def __init__(self, name):
        self.type = 'Boat'
        self.name = name
        super().__init__(name)


class CarBoat(Car, Boat):
    def __init__(self, name):
        self.type = 'CarBoat'
        self.name = name
        super().__init__(name)
