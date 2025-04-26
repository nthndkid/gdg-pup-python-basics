### **Description**

In this assignment, you will learn how to create and work with dictionaries in Python. A dictionary in Python is a collection of key-value pairs, where each key maps to a value. You will practice creating a dictionary, adding items, updating items, and removing items. Dictionaries are a useful data structure when you need to store and access data in a key-based format.

### **Expected Output**

The program should:

1. Create a dictionary with initial key-value pairs.
2. Add a new key-value pair.
3. Update an existing key-value pair.
4. Remove a key-value pair.
5. Display the dictionary after each operation.

Example output:

```
Original dictionary: {'name': 'Sparky', 'age': 25}
Dictionary after adding an item: {'name': 'Sparky', 'age': 25, 'city': 'New York'}
Dictionary after updating an item: {'name': 'Sparky', 'age': 26, 'city': 'New York'}
Dictionary after removing an item: {'name': 'Sparky', 'city': 'New York'}
```

---

### **Provided Files**

- `main.py` – The Python program that implements dictionary operations.

---

### **Instructions**

1. **Program Goal**:
   - Write a Python program that creates a dictionary and performs the following operations:
     - Add a new key-value pair using the dictionary's assignment syntax.
     - Update the value of an existing key.
     - Remove a key-value pair using the `del` statement or the `pop()` method.
2. **Steps**:
   - **Step 1**: Create a dictionary with at least two key-value pairs and print it.
     - Example dictionary: `{'name': 'Sparky', 'age': 25}`.
   - **Step 2**: Add a new key-value pair to the dictionary.
     - Add a `city` key with a value of `'New York'` and print the updated dictionary.
   - **Step 3**: Update an existing key-value pair.
     - Update the `age` key to `26` and print the updated dictionary.
   - **Step 4**: Remove a key-value pair.
     - Remove the `age` key and print the updated dictionary.
3. **Test the Program**:

   - Try different keys and values to ensure each operation works correctly.

4. **Before Reviewing the Provided File**:
   - Try implementing the assignment on your own first.
   - Use the provided file (`main.py`) only as a reference after you’ve attempted your own solution.

---

### **Tips**

- In a dictionary, you can access values using keys (e.g., `dictionary[key]`).
- The `del` statement is used to remove a key-value pair by specifying the key: `del dictionary[key]`.
- The `pop()` method also removes a key-value pair and returns the value.
- You can update an item by assigning a new value to an existing key (e.g., `dictionary[key] = new_value`).
- Try adding, updating, and removing different key-value pairs to see how the dictionary changes.
