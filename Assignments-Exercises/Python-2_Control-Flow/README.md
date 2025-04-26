# Python Assignment: Control Flow – If, Elif, Else & Try Catch

## Description

This exercise helps you practice using conditional statements (`if`, `elif`, `else`) and exception handling (`try`, `except`). You will:

- Check the age of the user and categorize them as a child, teenager, adult, or senior.
- Handle invalid inputs such as non-integer values or negative numbers gracefully.

## Expected Output

For valid input:

```
Please enter your age: 25
You are categorized as: Adult

Please enter your age: 10
You are categorized as: Child
```

For invalid input (e.g., non-numeric value or negative number):

```
# If the value is negative
Please enter your age: -10
Invalid input: Age cannot be negative.

# If the value is string
Please enter your age: test
Invalid input: invalid literal for int() with base 10: 'test'
```

## Provided Files

- `main.py` – The Python program that checks the age category based on user input.

## Provided Files

- `main.py` – The Python program that checks the age category based on user input.
- `README.md` – This README file.

## Instructions

Follow these steps to complete the assignment:

1. **Program Goal**:

   - Write a Python program that asks the user to input their age.
   - The program should:
     - Use `input()` to get the user’s response.
     - Use `int()` to convert the response to an integer.
     - Validate the input:
       - If the input is not a valid number (e.g., letters or symbols), display: "Invalid input: Age cannot be a non-number."
       - If the input is negative, display the message: `"Invalid input: Age cannot be negative."`

2. **Categorize the Age**:

   - Use conditional statements (`if`, `elif`, `else`) to categorize the user based on the age they entered:
     - If the age is below 13, display: `"You are categorized as: Child"`
     - If the age is between 13 and 19 (inclusive), display: `"You are categorized as: Teenager"`
     - If the age is between 20 and 59 (inclusive), display: `"You are categorized as: Adult"`
     - If the age is 60 or above, display: `"You are categorized as: Senior"`

3. **Error Handling**:

   - Use a `try` and `except` block to handle potential errors:
     - Catch and handle ValueError if the input cannot be converted to an integer.
     - Display "Invalid input: Age cannot be a non-number." for non-integer inputs.
     - For negative numbers, directly print: "Invalid input: Age cannot be negative." and do not categorize the input.

4. **Testing**:

   - Run the program multiple times to ensure it works correctly for:
     - Valid integer inputs (e.g., 5, 18, 45, 70).
     - Non-integer inputs (e.g., `abc`, `12.5`, `!@#`).
     - Negative numbers (e.g., `-10`).

5. **File Structure**:

   - Save your program in a file named `main.py`.
   - Write clean and readable code, including comments to explain what each part of the program does.

6. **Before Reviewing the Provided File**:
   - Try to implement the assignment on your own first.
   - Use the provided file (`main.py`) only as a reference after you’ve attempted your own solution.

## Tips

- Remember that the `input()` function always returns a string. Use `int()` to convert the input into an integer.
- Test the program with a variety of inputs to ensure it handles all cases, including edge cases.
- Use a try block to attempt conversion and an except block to handle invalid inputs
- Add comments to make your code clear and understandable.
