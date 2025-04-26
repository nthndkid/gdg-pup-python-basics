# Loops – For and While Assignment

# Part 1: For Loop - Printing a list of favorite foods
# Let's create a list of some favorite foods
favorite_foods = ['Pizza', 'Burger', 'Ice Cream', 'Pasta', 'Sushi']

# Using a for loop to print each food in the list
print("Here are my favorite foods:")
for food in favorite_foods:
    print(f"- {food}")  # Print each food item with a bullet point

print("\n")  # Add a blank line to separate the outputs of the two parts

# Part 2: While Loop - Countdown from a number
# Ask the user to enter a starting number for the countdown
try:
    starting_number = int(input("Enter a positive number to start the countdown: "))

    # Check if the number is positive
    if starting_number <= 0:
        print("Invalid input: Please enter a number greater than zero.")
    else:
        print("Countdown:")
        # Use a while loop to count down from the starting number to 1
        while starting_number > 0:
            print(starting_number)  # Print the current number
            starting_number -= 1   # Reduce the number by 1 for the next step

        print("Countdown complete!")  # Message when the countdown ends

# Handle invalid inputs (e.g., if the user enters a non-number)
except ValueError:
    print("Invalid input: Please enter a valid number.")
