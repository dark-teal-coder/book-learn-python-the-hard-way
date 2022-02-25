# Study Drills 13

# 1. Try giving fewer than three arguments to your script. 
# See that error you get? See if you can explain it.
# 2. Write a script that has fewer arguments and one that has more. 
# Make sure you give the unpacked variables good names.
# 3. Combine input with argv to make a script that gets more input from a user. 
# Don't overthink it. 
# Just use argv to get something, and input to get something else from the user.
# 4. Remember that modules give you features. Modules. Modules. 
# Remember this because we'll need it later.

# The argv is the argument variable. 
# This variable holds the arguments you pass to your Python script when you run it.
# These arguments come in as strings even though you input a number. 
from sys import argv

# # Unpack argv so that it gets assigned to N variables you can work with, 
# # rather than holding all the arguments.
# script, first, second, third = argv

# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# script, firstName, lastName = argv 
# print("Welcome, ", firstName, " ", lastName, "!", sep="")

script, firstName, lastName, school, major = argv 
print(f"{firstName} {lastName} is studying {major} at {school}.")

color = input("Enter your favorite color: ")
print(f"You like {color}.")