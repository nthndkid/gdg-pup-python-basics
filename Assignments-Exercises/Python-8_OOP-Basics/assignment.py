# 1. **Create the Car class**:
class Car:
    # constructor method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # describe method
    def describe(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# instance of Car 
# car = Car("Toyota", "Corolla", 2020)
car = Car("Toyota", "GR86 Kouki", 2024)
# Print and call the describe method of car class
print(car.describe())