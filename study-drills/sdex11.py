# Study Drills 11

# 1. Go online and find out what Python's input does.
# 2. Can you find other ways to use it? Try some of the samples you find.
# 3. Write another "form" like this to ask some other questions.

# Print "How old are you?".
# Instead of ending it with \n as default, end it with a space.
# After the space, take an input from the user and assign it to the variable age.
print("How old are you?", end=" ")
age = input()
# Print "How tall are you?".
# Instead of moving the cursor to the next line, move it to one space after.
# After the space, take an input from the user and assign it to the variable height.
print("How tall are you?", end=" ")
height = input()
# Similar to the above explanation. 
print("How much do you weigh?", end=" ")
weight = input()

# Take the values from age, height and weight.
# Put them in the placeholders {age}, {height} and {weight}, respectively.
print("So, you're {age} old, {height} tall and {weight} heavy.")

# # Take the values from age, height and weight.
# # Assign them as raw data to the placeholders {0!r}, {1!r} and {2!r}, respectively.
# print("So, you're {0!r} old, {1!r} tall and {2!r} heavy.".format(age, height, weight))

# NOTES: 
# Python 2: print "item"
# Python 3: print("item")
# Python 2: print "item1", 2
# Python 3: print("item1", 2)
# Python 2: print x,
# Python 3: print(x, end=" ")
# Python 2: print
# Python 3: print()
# Python 2: raw_input()
# Python 3: input()
# Python 2: input()
# Python 3: eval(input())
# Python 2: print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
# Python 3: print("So, you're {0!r} old, {1!r} tall and {2!r} heavy.".format(age, height, weight))

print("What's your name?", end=" ")
name = input()
print("How many hours do you sleep every day?", end=" ")
sleep = int(input())
print("How many hours do you spend on eating every day?", end=" ")
eat = int(input())
print("How many minutes do you spend on showering every day?", end=" ")
showerMin = int(input())
shower = showerMin / 60

timeLeft = 24 - sleep - eat - shower
print("Hi there, ", name, "! You only have ", timeLeft, " hours left in a day.", sep="")