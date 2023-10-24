from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def __init__(self, max_speed, current_speed):
        self.max_speed = max_speed
        self.current_speed = current_speed

    def start_engine(self):
        return "car started"

    def stop_engine(self):
        self.current_speed = 0
        return "car stopped"

class SportCar(Car):
    def start_engine(self):
        return super().start_engine() + f", max speed is {self.max_speed}"

    def stop_engine(self):
        super().stop_engine()
