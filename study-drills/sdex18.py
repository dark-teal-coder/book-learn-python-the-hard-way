# Study Drills 18

# Create a function checklist for later exercises. 
# 1. Did you start your function definition with def?
# 2. Does your function name have only characters and _ (underscore) characters?
# 3. Did you put an open parenthesis right after the function name?
# 4. Did you put your arguments after the parenthesis separated by commas?
# 5. Did you make each argument unique (meaning no duplicated names)?
# 6. Did you put a close parenthesis and a colon after the arguments?
# 7. Did you indent all lines of code you want in the function four spaces? No more, no less.
# 8. Did you "end" your function by going back to writing with no indent (dedenting, we call it)?
# When you run ("use" or "call") a function, check these things:
# 1. Did you call/use/run this function by typing its name?
# 2. Did you put the ( character after the name to run it?
# 3. Did you put the values you want into the parentheses separated by commas?
# 4. Did you end the function call with a ) character?
# Use these two checklists on the remaining lessons until you do not need them anymore.
# Finally, repeat this a few times to yourself: 
# To "run", "call", or "use" a function each means the same thing.

# NOTES:
# Functions do three things:
    # 1. They name pieces of code the way variables name strings and numbers.
    # 2. They take arguments the way your scripts take argv.
    # 3. Using 1 and 2, they let you make your own "mini-scripts" or "tiny commands".
# Syntax of functions:
# def functionName(parameters):
    # block of statements

# After the colon, all the lines indented 4 spaces will become attached to print_two.
# A function has a fixed number of arguments. 
# We need the variadic arguments to handle an arbitrary number of runners. 
    # *args for the arbitrary numbers of positional arguments (required)
    # **kwargs for the arbitrary numbers of keyword arguments (optional)
# *args takes all the arguments to the function and then puts them in args as a list.
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument.
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguments.
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# NOTES:
# Only positional arguments:
def printName1(*args):
    print(args) # Output: ('John', 'Alice', 'Tom', 'Wilson')
    print(*args) # Output: John Alice Tom Wilson
printName1("John", "Alice", "Tom", "Wilson")
# Only keyword arguments:
def printName2(**kwargs):
    print(kwargs) # Output: {'first': 'John', 'second': 'Alice', 'fourth': 'Wilson', 'third': 'Tom'}
printName2(first="John", second="Alice", fourth="Wilson", third="Tom")
# Both positional arguments and keyword arguments: 
def printName3(*args, **kwargs):
    print(args) # Output: ('John', 'Alice')  
    print(kwargs) # Output: {'third': 'Tom', 'fourth': 'Wilson'}
printName3("John", "Alice", third="Tom", fourth="Wilson")
# The keyword arguments cannot be declared before positional arguments.

# NOTES:
num = [1, 2, 3, 4, 5]
def printNum1(*args):
    print(*args) # Output: 1 2 3 4 5

def printNum2(*args):
    print(args) # Output: (1, 2, 3, 4, 5)

printNum1(*num)
printNum2(*num)