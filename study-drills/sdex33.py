# Study Drills 33

# 1. Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
# 2. Use this function to rewrite the script to try different numbers.
# 3. Add another variable to the function arguments that you can pass in that lets you change the
# + 1 on line 8 so you can change how much it increments by.
# 4. Rewrite the script again to use this function to see what effect that has.
# 5. Write it to use for-loops and range. Do you need the incrementor in the middle anymore?
# What happens if you do not get rid of it?

# NOTES: 
# A while-loop tests the condition and runs the code block until the expression is False. 
# Unlike an if-statement which runs the code block once, it jumps back to the top of "while" and repeats.
# While-loops do not stop so we want to end them at some point. 
# Some rules:
# 1. Use while-loops sparingly. A for-loop is preferred. 
# 2. Make sure that the Boolean test will become False at some point.
# 3. When in doubt, print out your test variable at the top and bottom of the while-loop.
# Difference between between for-loop and while-loop:
    # A for-loop can only iterate (loop) over collections of things.
    # A while-loop can do any kind of iteration (looping).
    # The while-loops are harder to get right. 

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)

# Convert the while-loop to a function:

numbers1 = []

def function1(j):
    print(f"At the top j is {j}")
    numbers1.append(j)
    j += 1
    print("Numbers now: ", numbers1)
    print(f"At the bottom j is {j}")
    # if j != 6: 
    # if j < 6: 
    if j in numbers:
        function1(j)

function1(0)

print("The numbers: ")

for num1 in numbers1:
    print(num1)

# Add increment variable t: 

numbers2 = []

def function2(r, s, t):
    print(f"At the top r is {r}")
    numbers2.append(r)
    r += t
    print("Numbers now: ", numbers2)
    print(f"At the bottom r is {r}")
    if r < s:
        function2(r, s, t)

function2(0, 6, 2)

print("The numbers: ")

for num2 in numbers2:
    print(num2)

# Use for-loops and range():

numbers3 = []

def function3(r, s, t):
    for i in range(r, s, t):
        print(f"At the top r is {i}")
        numbers3.append(i)
        i += t
        # i += t will only affect the variable i below this line within the current iteration.
        # The next iteration i will still be (r+t)
        print("Numbers now: ", numbers3)
        print(f"At the bottom r is {i}")

function3(0, 20, 3)

print("The numbers: ")

for num3 in numbers3:
    print(num3)