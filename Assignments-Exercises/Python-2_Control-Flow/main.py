# This program checks the age and categorizes the person into different age groups.
# It also demonstrates exception handling using try and except.

try:
    # Input: Get age from the user
    user_input = int(input("Please enter your age: "))

    # Check the age category
    if user_input < 0:
        raise ValueError("Age cannot be negative.")
    elif user_input < 13:
        print("You are categorized as: Child")
    elif user_input < 20:
        print("You are categorized as: Teenager")
    elif user_input < 60:
        print("You are categorized as: Adult")
    else:
        print("You are categorized as: Senior")
        
except ValueError:
    print("Invalid input: Age cannot be a non-number.")
