# Study Drills 28

# 1. There are a lot of operators in Python similar to != and ==. 
# Try to find as many "equality operators" as you can. They should be like < or <=.
# 2. Write out the names of each of these equality operators. 
# For example, I call != "not equal".
# 3. Play with Python by typing out new Boolean operators, 
# and before you press Enter try to shout out what it is. 
# Do not think about it. Shout the first thing that comes to mind. 
# Write it down, then press Enter, and keep track of how many you get right and wrong.
# 4. Throw away the piece of paper from 3 so you do not accidentally try to use it later.

# Equality operators: 
    # <>: If values of two operands are not equal, then condition becomes true. 
    # !=: If values of two operands are not equal, then condition becomes true.	

# <> ("less than or greater than") VS. != ("not equal to"):
    # Similar but Python has deprecated <> in favor of !=.

# Identity operators: 
    # is: True if the operands are identical (refer to the same object)
    # is not: True if the operands are not identical (not refer to the same object)
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]
print(x1 is not y1) # Output: False
print(x2 is y2) # Output: True
print(x3 is y3) # Output: False
# x1 and y1 are integers of same values so they are equal as well as identical. 
# Same is the case with x2 and y2 (strings).
# But x3 and y3 are list. They are equal but not identical. 
# It is because interpreter locates them separately in memory although they are equal.

# is ("identical to") VS. == ("equal to"): 
    # The is operator and the equality operator are not same. 
    # is checks if both the variables point to the same object.
    # == sign checks if the values for the two variables are the same.

# NOTES:
# Process to solve Boolean logic statements:
    # 1. Find an equality test (== or !=) and replace it with its truth.
    # 2. Find each and/or inside parentheses and solve those first.
    # 3. Find each not and invert it.
    # 4. Find any remaining and/or and solve it.
    # 5. When you are done you should have True or False.
