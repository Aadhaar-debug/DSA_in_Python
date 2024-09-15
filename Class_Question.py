'''
You are tasked with creating a simple system to represent different types of vehicles. You need to create a base class 
Vehicle and two derived classes: Car and Bike. Each vehicle will have a make, model, and year. The base class Vehicle 
should have a method start_engine() which prints "Starting engine...".

The Car class should inherit from Vehicle and override the start_engine() method to print "Starting car engine...". 
Additionally, it should have a unique method open_trunk() that prints "Opening trunk...".

The Bike class should inherit from Vehicle and override the start_engine() method to print "Starting bike engine...". 
It should also have a unique method kickstand() that prints "Engaging kickstand...".

Tasks:
Create the base class Vehicle.
Create the derived classes Car and Bike with the specified methods.
Demonstrate the functionality by creating instances of both Car and Bike and calling their methods.
'''

class Vehicle:
    def __init__(self , make , model , year):
        self.make = make
        self.model = model
        self.year = year
    def start_engine(self):
        print("Starting engine...")

class Car(Vehicle):
    def start_engine(self):
        print("Starting car engine...")
    def open_trunk(self):
        print("Opening trunk...")

class Bike(Vehicle):
    def start_engine(self):
        print("Starting bike engine...")
    def kickstand(self):
        print("Engaging kickstand...")


car = Car("Tesla", "Model S", 2023)
car.start_engine()  # Should print "Starting car engine..."
car.open_trunk()    # Should print "Opening trunk..."

bike = Bike("Yamaha", "MT-09", 2022)
bike.start_engine()  # Should print "Starting bike engine..."
bike.kickstand()     # Should print "Engaging kickstand..."