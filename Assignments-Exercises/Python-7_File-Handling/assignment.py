
"""
    -**Step 2**: In your Python program, use the `open()` function to open the file in read mode (`'r'`).
    - Use the `read()` or `readlines()` method to read the contents of the file.
    - Print the contents of the file to the console.
"""
try:
    with open('pytestfile.txt', 'r') as file:
        content = file.read()
        print("Contents of the file: \n")
        print(content + "\n")
except FileNotFoundError:
    print("'pytestfile.txt' was not found.")

"""
    - **Step 3**: Create a new file named `newfile.txt` using the `open()` function in write mode (`'w'`).
    - Write some content to the file using the `write()` method.
    - Close the file after writing the content.
"""
with open('newfile.txt', 'w') as file:
    file.write("Created new file form Assigment 7." + "\nTest add")
    print("New file created:")

"""
   - **Step 4**: Optionally, read the contents of the newly created file to 
   ensure that the content was written correctly.
"""
# # Step 3: Verify content in the new file by reading it
with open('newfile.txt', 'r') as file:
    file_content = file.read()
    print(file_content)