from abc import ABC
from car import Car
from tires import tire_wear_sensors


class CarriganTires(Car, ABC):
    def __init__(self, arr):
        self.v1 = arr[0]
        self.v2 = arr[1]
        self.v3 = arr[2]
        self.v4 = arr[3]

    def needs_service(self):
        if self.v1 >= 0.9 or self.v2 >= 0.9 or self.v3 >= 0.9 or self.v4 >= 0.9 :
            return True
        else:
            return False