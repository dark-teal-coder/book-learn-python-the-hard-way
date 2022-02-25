# Study Drills 21

# 1. If you aren't really sure what return does, 
# try writing a few of your own functions and have them return some values. 
# You can return anything that you can put to the right of an =.
# 2. At the end of the script is a puzzle. 
# I'm taking the return value of one function and using it as the argument of another function. 
# I'm doing this in a chain so that I'm kind of creating a formula using the functions. 
# It looks really weird, but if you run the script, you can see the results.
# What you should do is try to figure out the normal formula that would recreate this same set of operations.
# 3. Once you have the formula worked out for the puzzle, 
# get in there and see what happens when you modify the parts of the functions. 
# Try to change it on purpose to make another value.
# 4. Do the inverse. Write a simple formula and use the functions in the same way to calculate it.

from math import pi

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

def power(a, b):
    print(f"CALCULATING {a} raised to the power of {b}")
    return a ** b

print(f"2 ** 3 = {power(2, 3)}")

r = float(input("Enter the radius to calculate the sphere volumn: "))

sphere_volumn = multiply(divide(4, 3), multiply(pi, power(r, 3)))

print(f"When r = {r}, Sphere Volumn V = 4/3πr^3 = {sphere_volumn}")