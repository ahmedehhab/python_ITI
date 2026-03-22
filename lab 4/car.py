import math

class Car:

    def __init__(self, name, fuelRate=100, velocity=0):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        self.__fuelRate = max(0, min(100, value))

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, value):
        self.__velocity = max(0, min(200, value))

    def run(self, velocity, distance):
        self.velocity = velocity
        self.fuelRate -= math.floor(distance / 10) * 10

        if self.fuelRate <= 0:
            self.stop(distance / 2)
        else:
            self.stop(0)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance > 0:
            print(f"stopped, {remain_distance} km remaining")
        else:
            print("arrived")