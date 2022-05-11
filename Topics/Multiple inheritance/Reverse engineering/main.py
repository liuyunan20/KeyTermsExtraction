# create the hierarchy here
class Vehicle:
    def __init__(self):
        self.type = 'Vehicle'


class LandVehicle(Vehicle):
    def __init__(self):
        self.type = 'LandVehicle'
        super().__init__()


class WaterVehicle(Vehicle):
    def __init__(self):
        self.type = 'WaterVehicle'
        super().__init__()


class Car(LandVehicle):
    def __init__(self):
        self.type = 'Car'
        super().__init__()


class Boat(WaterVehicle):
    def __init__(self):
        self.type = 'Boat'
        super().__init__()


class CarBoat(Car, Boat):
    def __init__(self):
        self.type = 'CarBoat'
        super().__init__()
