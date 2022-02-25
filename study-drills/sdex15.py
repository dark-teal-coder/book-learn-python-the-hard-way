# Study Drills 15

# 1. Above each line, comment out in English what that line does.
# 2. If you are not sure, ask someone for help or search online. 
# Searching for "python3.6 THING" will find answers to what THING does in Python. 
# Try searching for "python3.6 open."
# 3. I used the word "commands" here, but commands are also called "functions" and "methods".
# You will learn about functions and methods later in the book.
# 4. Get rid of lines 10–15 where you use input and run the script again.
# 5. Use only input and try the script that way. 
# Why is one way of getting the filename better than another?
# 6. Start python3.6 to start the python3.6 shell, 
# and use open from the prompt just like in this program. 
# Notice how you can open files and run read on them from within python3.6?
# 7. Have your script also call close() on the txt and txt_again variables. 
# It’s important to close files when you are done with them.

# sys.argv is the list of arguments from the command line.
from sys import argv

# Not to hard code the file name into our script.
# i.e. Not to put some info that should come from the user as a string directly in our source code.
# We want it to load other files later. 
# Solution: to use argv or input to ask the user for the file's name to open.
script, filename = argv

# Open the file with the file name from the 2nd argument [1] on the command line. 
# Call the file object txt. 
txt = open(filename) 

# Get the file name as a string from the 2nd argument [1] from the commmand line.
# Replace {} with it in the formatted string. Print the string. 
print(f"Here's your file {filename}:")
# The method read() reads at most size bytes from the file. 
# If the read hits EOF before obtaining size bytes, then it reads only available bytes.
# Syntax: fileObject.read(size)
# Size = the number of bytes to be read from the file
print(txt.read())

# Print the string.
print("Type the filename again:")
# Prompt the user with "> " and get the user input.
# Assign it to the variable file_again. 
file_again = input("> ")

# Open the file with the name from the user input. 
# Create a file object called txt_again. 
txt_again = open(file_again)

# Read the file object called txt_again. 
print(txt_again.read())

txt.close()
txt_again.close()