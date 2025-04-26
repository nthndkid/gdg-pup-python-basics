# Step 1: Read contents from a file
try:
    with open('sample.txt', 'r') as file:
        contents = file.read()
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")

# Step 2: Write to a new file
with open('newfile.txt', 'w') as file:
    file.write("This is a new file, like New Year New Me XD.\n")
    print("\nNew file created with content:")

# Step 3: Verify content in the new file by reading it
with open('newfile.txt', 'r') as file:
    newfile_contents = file.read()
    print(newfile_contents)