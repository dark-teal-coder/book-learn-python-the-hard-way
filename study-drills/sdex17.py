# Study Drills 17

# 1. This script is really annoying. 
# There's no need to ask you before doing the copy, and it prints too much out to the screen. 
# Try to make the script more friendly to use by removing features.
# 2. See how short you can make the script. I could make this one line long.
# 3. Notice at the end of the What You Should See section I used something called cat? 
# It's an old command that concatenates files together, 
# but mostly it's just an easy way to print a file to the screen. 
# Type man cat to read about it.
# 4. Find out why you had to write out_file.close() in the code.
# 5. Go read up on Python's import statement, and start python3.6 to try it out. 
# Try importing some things and see if you can get it right. 
# It's alright if you do not.

# import: to access another module by importing the file/function
# Syntax 1: 
    # import math 
    # print(math.pi) 
# Syntax 2: 
    # from math import pi 
    # print(pi) 
# Syntax 3: 
    # from math import *
    # print(pi)
from sys import argv
# os.path.exists(path) returns True if path refers to an existing path/an open file descriptor. 
from os.path import exists

# from_file must exist while to_file may or may not exist. 
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# Open the file object with the file name from from_file in read-only mode. 
in_file = open(from_file)
# read() returns the content from the file object in a string format. 
indata = in_file.read()
# # Python will automatically chose the file if written in one line as:
# indata = open(from_file).read()

# 1. Remove lines 12-16 in ex17.py to make it more friendly. 

# print(f"The input file is {len(indata)} bytes long")
# # exists() returns True if a file exists, based on its name.
# print(f"Does the output file exist? {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# # Get the user to hit RETURN or CTRL-C. 
# input()

# Open/Create the file object with the file name from to_file in write-only mode. 
out_file = open(to_file, 'w')
# Get the string content and write it to the file with the name from to_file. 
out_file.write(indata)

print("Alright, all done.")

# You should always close your files.
# Changes made to a file may not show until you close the file due to buffering. 
out_file.close()
in_file.close()

# 2. My shorest script:
# from sys import argv 
# script, from_file, to_file = argv
# open(to_file, 'w').write(open(from_file).read())

# One line of code (using ;): 
# from sys import argv; script, from_file, to_file = argv; open(to_file, 'w').write(open(from_file).read())