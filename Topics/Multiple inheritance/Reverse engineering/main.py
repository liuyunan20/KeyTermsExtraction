# create the hierarchy here
class Vehicle:
    ...


class LandVehicle(Vehicle):
    ...


class WaterVehicle(Vehicle):
    ...


class Car(LandVehicle):
    ...


class Boat(WaterVehicle):
    ...


class CarBoat(Car, Boat):
    ...
