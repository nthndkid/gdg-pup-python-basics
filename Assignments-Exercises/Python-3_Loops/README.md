Here's the assignment for **Loops – For and While**:

---

## Provided Files

- `main.py` – The Python program containing examples of both `for` and `while` loops.

---

## Instructions

Follow these steps to complete the assignment:

---

### 1. **Program Goal**:

- Write a Python program that demonstrates the use of both `for` and `while` loops.
- The program will have two main parts:
  1.  **Iterating Through a List Using a `for` Loop**:
      - Create a list of at least five of your favorite foods (e.g., `['pizza', 'sushi', 'pasta', 'tacos', 'ice cream']`).
      - Use a `for` loop to iterate through the list and print each food item on a new line.
  2.  **Countdown Using a `while` Loop**:
      - Ask the user for a starting number (e.g., `10`).
      - Use a `while` loop to count down from the starting number to `1`, printing each number.
      - After reaching `1`, print `"Countdown complete!"`.

---

### 2. **Requirements**:

- **For Loop Section**:
  - Create a list of your favorite items (foods, movies, colors, etc.).
  - Use a `for` loop to iterate through the list and print each item.
- **While Loop Section**:
  - Prompt the user to enter a positive integer as the starting number.
  - Validate the input:
    - If the input is not a valid positive integer, display: `"Invalid input: Please enter a number greater than zero."`
    - If the input is valid, start the countdown.
  - Use a `while` loop to count down from the starting number to `1`.
  - Once the countdown reaches `1`, print `"Countdown complete!"`.

---

### 3. **Error Handling**:

- Use a `try` and `except` block to handle invalid inputs for the starting number in the countdown.
- Display an appropriate error message (`"Invalid input: Please enter a positive integer."`) for non-integer or negative inputs.

---

### 4. **Testing**:

- Run the program multiple times to ensure it works correctly for:
  - A valid list of items in the `for` loop.
  - Valid and invalid inputs for the starting number in the `while` loop.

---

### 5. **File Structure**:

- Save your program in a file named `main.py`.
- Ensure your code is clean and readable, with comments to explain each section.

---

### 6. **Before Reviewing the Provided File**:

- Attempt to complete the assignment on your own first.
- Use the provided file (`main.py`) as a reference only after trying it yourself.

---

## Tips

- Use a `for` loop for iterating through a collection (like a list) to access each item one by one.
- Use a `while` loop when the number of iterations depends on a condition.
- The `input()` function returns a string, so you must convert it to an integer using `int()` when necessary.
- Use comments to describe the purpose of each part of your code for better readability.
