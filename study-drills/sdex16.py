# Study Drills 16

# 1. If you do not understand this, 
# go back through and use the comment trick to get it squared away in your mind. 
# One simple English comment above each line will help you understand 
# or at least let you know what you need to research more.
# 2. Write a script similar to the last exercise that uses read and argv 
# to read the file you just created.
# 3. There's too much repetition in this file. 
# Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
# 4. Find out why we had to pass a 'w' as an extra parameter to open. 
# Hint: open tries to be safe by making you explicitly say you want to write a file.
# 5. If you open the file with 'w' mode, then do you really need the target.truncate()? 
# Read the documentation for Python's open function and see if that's true.

# NOTES:
# close(): 
    # It closes an open file. Like File > Save in your editor.
# read(): 
    # It reads the contents of the file. 
# readline(): 
    # It returns just one line of a text file.
    # Calling readline() N times will return N lines of the file. 
# truncate(): 
    # It empties the file. Watch out!
    # truncate(size) resizes the file to the given number of bytes.
# write('stuff'): 
    # It writes "stuff" to the file.
    # write() takes a parameter of a string you want to write to the file.
# seek(0): 
    # It moves the read/write location to the beginning of the file.
    # It sets the current file position in a file stream.

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Prompt the user to hit CTRL-C or RETURN.
input("?")

print("Opening the file...")
# The 2nd argument of open() specifies the mode for the file. 
# 'w' for 'write' mode
    # open(filename, 'w') will create a new file if it does not already exist.
    # The file is truncated and overwritten if it already exists.
# 'r' for 'read' mode
    # open(filename, 'r') can only open the file that already exists in read-only mode.
# 'a' for 'append' 
    # open(filename, 'a') opens the file in write-only mode.
    # It will create a new file if it does not already exist.
    # The data you write is appended to what's already in the file.
# The default is 'r' so open(file) is equal to open(file, 'r')
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# Truncating a file to zero means discarding all its content.
# The file size becomes 0 so it becomes empty.
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# # Write the string from the user input in line1 to the file. 
# target.write(line1)
# # Write a line or move the cursor to the next. 
# target.write("\n")
# # Write the string from the user input in line2 to the file.
# target.write(line2)
# target.write("\n")
# # Write the string from the user input in line3 to the file.
# target.write(line3)
# target.write("\n")

# Combine them into one line.
target.write(f"{line1}\n{line2}\n{line3}\n")

# Close the file to commit it before read() it. 
target.close() 

content = open(filename, 'r')
print(content.read())

print("And finally, we close it.")

# If we put target.close() here, the file isn't saved before being read.
# It can't print the text out. 
content.close()

# target.truncate() is unnecessary if the file is open in 'w' mode. 