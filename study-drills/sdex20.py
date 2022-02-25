# Study Drills 20

# 1. Write an English comment for each line to understand what that line does.
# 2. Each time print_a_line is run, you are passing in a variable, current_line. 
# Write out what current_line is equal to on each function call, 
# and trace how it becomes line_count in print_a_line.
# 3. Find each place a function is used, 
# and check its def to make sure that you are giving it the right arguments.
# 4. Research online what the seek function for file does. 
# Try pydoc file, and see if you can figure it out from there. 
# Then try pydoc file.seek to see what seek does.
# 5. Research the shorthand notation +=, and rewrite the script to use += instead.

# sys.argv is the list of arguments from the command line.
from sys import argv

# Unpack argv to get each value assigned to the variables on the left. 
script, input_file = argv

# Define a function with the name print_all. 
# Create an argument slot called f. 
def print_all(f):
    # Print the content of f where f is a file object opened in read-only mode. 
    # read() can only be called on a file object so f has to be a file.
    print(f.read())

# Define a function with the name rewind.
# Create an argument slot called f.
def rewind(f):
    # seek(offset, from_what) sets the current file position in a file stream.
    # from_what value = reference point (0, 1 or 2)
    # 0 = the beginning of the file; 1 = the current file position; 2 = the end of the file
    # seek(0) sets the current file position to the beginning of the file.
    f.seek(0)

# Define a function with the name print_a_line. 
# Create two argument slots called line_count and f. 
def print_a_line(line_count, f):
    # Print the value the variable line_count refers to
    # Print a line from the file f after a space. 
    print(line_count, f.readline())

# Open the file with the name from input_file in read-only mode and call it current_file.
current_file = open(input_file)

# Print the string with a line character inside.
print("First let's print the whole file:\n")

# Call the function print_all and pass the file-object argument from current_file to it.
print_all(current_file)

# Print the string. 
print("Now let's rewind, kind of like a tape.")

# Call the function rewind and pass the file-object argument from current_file to it.
rewind(current_file)

# Print the string. 
print("Let's print three lines:")

# Assign 1 to the variable current_line.
current_line = 1
# Call the function print_a_line.
# Pass the arguments current_line (i.e. 1) and current_file to it.
# Match the 1st slot called current_line here to that of the function called line_count. 
# Match the 2nd slot called current_file here to that of the function called f.
print_a_line(current_line, current_file)

# Add 1 to the current value of current_line (i.e. 1).
# Assign the new value (i.e. 2) to current_line.
# current_line = current_line + 1
current_line += 1
# Call the function print_a_line again.
# Pass the arguments current_line (i.e. 2) and current_file to it.
# Match the 1st slot called current_line here to that of the function called line_count. 
# Match the 2nd slot called current_file here to that of the function called f.
print_a_line(current_line, current_file)

# Add 1 to the current value of current_line (i.e. 2).
# Assign the new value (i.e. 3) to current_line.
# current_line = current_line + 1
current_line += 1
# Call the function print_a_line again.
# Pass the arguments current_line (i.e. 3) and current_file to it.
# Match the 1st slot called current_line here to that of the function called line_count. 
# Match the 2nd slot called current_file here to that of the function called f.
print_a_line(current_line, current_file)