# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

#inorder to use an abstract class, it mus be imported
    #abc: stand for (abstract-base-class)
    #import:(ABC) class, abstractmethod

from abc import ABC, abstractmethod

#the class intended to be the abstract class inherits (ABC) class
class Vehicle(ABC):

    #any abstract method must come w/ decerator    @abstractmethod

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")
        return self

    def stop(self):
        print("This motorcycle is stopped")

car = Car()
car.go() + "<----------------------------------------------"
