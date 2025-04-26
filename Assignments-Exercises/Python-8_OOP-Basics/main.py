# Define the Car class
class Car:
    # The constructor method to initialize the object
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to return a description of the car
    def describe(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Print the description of the car
print(my_car.describe())
