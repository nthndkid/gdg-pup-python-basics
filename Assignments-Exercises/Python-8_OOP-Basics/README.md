# OOP Basics - Car Class

## Description

This assignment introduces you to Object-Oriented Programming (OOP) in Python. You will create a class called `Car` that models a real-world car. The class will have attributes such as `make`, `model`, and `year`, and a method called `describe` that returns a string describing the car.

## Expected Output

When the program is run, it will create an instance of the `Car` class and print a description of the car. For example:

```
This car is a 2020 Toyota Corolla.
```

## Provided Files

- `main.py` – The Python program where the Car class is defined and instantiated.

## Instructions

1. **Create the Car class**:

   - Define a class called `Car`.
   - Add a constructor method (`__init__`) to initialize the car’s `make`, `model`, and `year` attributes.

2. **Add the describe method**:

   - Create a method called `describe` that returns a string with the description of the car (e.g., "This car is a 2020 Toyota Corolla.").

3. **Create an instance of the class**:

   - In the main program, create an instance of the `Car` class with your chosen make, model, and year.
   - Call the `describe` method on the object and print the result.

4. **Testing**:
   - Test your code by creating different instances of the `Car` class with different values for `make`, `model`, and `year`.
   - Print the description for each car instance.

## Tips

- Remember that when you define a class, the constructor method (`__init__`) is used to initialize attributes for objects created from that class.
- The `self` parameter in the methods refers to the instance of the class (the object).
- Try creating multiple instances of the `Car` class to test your program with different car details.
- You can later extend this class by adding more attributes (like `color` or `mileage`) or more methods (like `start` or `stop`).

## Before Reviewing the Provided File

- Try to implement the assignment on your own first.
- Use the provided file (`main.py`) only as a reference after you’ve attempted your own solution.
