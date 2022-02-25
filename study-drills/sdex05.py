# Study Drills 05

# 1. Change all the variables so there is no my_ in front of each one. 
# Make sure you change the name everywhere, not just where you used = to set them.
# 2. Try to write some variables that convert the inches and pounds to centimeters and kilograms.
# Do not just type in the measurements. Work out the math in Python.

import datetime
now = datetime.datetime.now()

myName = 'Preesa Wong'
myAge = 35 # not a lie
myHeight = 74 # inches
myWeight = 180 # lbs
myEyes = 'Blue'
myTeeth = 'White'
myHair = 'Brown'

# {} to embed variables inside a string at where {} is. 
# f before double-quote tells Python 3 that the string needs to be formatted.
# Put the value my_name refers to in {} in the string. 
# Output: "Let's talk about Preesa Wong."
print(f"Let's talk about {myName}.")
print(f"He's {myHeight} inches tall.")
print(f"He's {myWeight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {myEyes} eyes and {myHair} hair.")
print(f"His teeth are usually {myTeeth} depending on the coffee.")
total = myAge + myHeight + myWeight
print(f"If I add {myAge}, {myHeight}, and {myWeight} I get {total}.")

# print("Let's talk about {0:s}.".format(myName))
# print("He's {0:d} inches tall.".format(myHeight))
# print("He's {0:d} pounds heavy.".format(myWeight))
# print("Actually that's not too heavy.")
# print("He's got {0:s} eyes and {1:s} hair.".format(myEyes, myHair))
# print("His teeth are usually {0:s} depending on the coffee.".format(myTeeth))
# print("If I add {0:d}, {1:d}, and {2:d} I get {3:d}.".format(myAge, myHeight, myWeight, 
# myAge + myHeight + myWeight))

inch = 1
cm = inch * 2.54 
print("{0:.2f} inches = {1:.2f} centimeters".format(inch, cm))
pound = 1
kg = pound * 0.453592
print("{0:.2f} pounds = {1:.2f} kilograms".format(pound, kg))

# NOTES:
# Python 2: r%
# Python 3: r!
# 2019-06-14 17:28:36.114771
print("Using \"{0}\".format(datetime.datetime.now())", "\t", "{0}".format(now))
# datetime.datetime(2019, 6, 14, 17, 28, 36, 114771)
print("Using \"{0!r}\".format(datetime.datetime.now())", "\t", "{0!r}".format(now))

# 7.1.3.1. Format Specification Mini-Language: 
# https://docs.python.org/2/library/string.html#formatspec