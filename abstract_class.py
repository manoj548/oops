from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass


class Bike(Vehicle):
    def start(self):
        print("Bike can be start using key or button")

    def stop(self):
        print("Bike can stop using key")

class Car(Vehicle):
    def start(self):
        print("Car can be start using key or button")

    def stop(self):
        print("car can stop using key or button")

obj  = Bike()
obj.start()
obj.stop()

obj1 = Car()
obj1.start()
obj1.stop()


