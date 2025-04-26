### **Description**

In this assignment, you will learn how to handle files in Python. You will work with two basic file operations: reading from a file and writing to a file. You will create a Python program that opens a file, reads its contents, and displays it. Additionally, you will practice creating a new file and writing data into it.

### **Expected Output**

The program should:

1. Open a file for reading.
2. Read the contents of the file.
3. Display the contents of the file.
4. Optionally, create a new file and write some content to it.

Example output:

```
Contents of the file:
Hello, this is a test file.
Python file handling is easy and fun!

New file created with content:
This is a new file, like New Year New Me XD
```

---

### **Provided Files**

- `main.py` – The Python program for file handling operations.
- `sample.txt` – A sample file with some content for reading.

---

### **Instructions**

1. **Program Goal**:

   - Write a Python program that:
     - Reads the contents of a file and prints it to the console.
     - Creates a new file and writes content to it.

2. **Steps**:

   - **Step 1**: Create a file named `sample.txt` (or use any existing file you have) and add some text to it, such as:
     ```
     Hello, this is a test file.
     Python file handling is easy and fun!
     ```
   - **Step 2**: In your Python program, use the `open()` function to open the file in read mode (`'r'`).
     - Use the `read()` or `readlines()` method to read the contents of the file.
     - Print the contents of the file to the console.
   - **Step 3**: Create a new file named `newfile.txt` using the `open()` function in write mode (`'w'`).
     - Write some content to the file using the `write()` method.
     - Close the file after writing the content.
   - **Step 4**: Optionally, read the contents of the newly created file to ensure that the content was written correctly.

3. **Test the Program**:

   - Ensure that the program reads the content from `sample.txt` and displays it correctly.
   - Verify that the program creates a new file (`newfile.txt`) and writes content into it.

4. **Before Reviewing the Provided File**:
   - Try implementing the assignment on your own first.
   - Use the provided file (`main.py`) only as a reference after you’ve attempted your own solution.

---

### **Tips**

- Use `open('filename', 'r')` to open a file for reading, and `open('filename', 'w')` to open a file for writing.
- The `read()` method reads the entire file, while the `readlines()` method reads each line of the file into a list.
- Remember to close the file using `file.close()` after reading or writing to ensure resources are properly released.
- When using write mode (`'w'`), if the file already exists, it will be overwritten.
- To append to an existing file, use `'a'` mode when opening the file.

---

### **What You Need to Submit**

1. **main.py** – Your Python program that reads from and writes to files.
2. **README.md** – This file with detailed instructions.
3. **sample.txt** – A file with sample content (if needed for reading).
4. **newfile.txt** – The file you created and wrote content to.
