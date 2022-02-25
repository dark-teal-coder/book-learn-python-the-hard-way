# Study Drills 30

# 1. Try to guess what elif and else are doing.
# 2. Change the numbers of cars, people, and trucks, 
# and then trace through each if-statement to see what will be printed.
# 3. Try some more complex Boolean expressions like cars > people or trucks < cars.
# 4. Above each line write a comment describing what the line does.

# MY ANSWERS:
# 1. If the if-statement is evaluated to False, Python will check the elif-statements.
# If all the if- and elif-statements are evaluated to False, Python will check the else-statement.

# Assign 30 to people 
people = 30
# Assign 40 to cars
cars = 20
# Assign 15 to trucks 
trucks = 15 # Try to change from 15 to 45

# If the value of cars is greater than that of people, print the statement.
if cars > people:
	print("We should take the cars.")
# Otherwise, check if the value of cars is less than that of people.
# If the value of cars is less than that of people, print the statement. 
elif cars < people: 
    print("We should not take the cars.")
# If the value of cars isn't greater than or less than that of people, print the statement.
else:
    print("We can't decide.")

# If the value of trucks is greater than that of cars, print the statement.
if trucks > cars:
    print("That's too many trucks.")
# Otherwise, check if the value of trucks is less than that of cars. 
# If the value of trucks is less than that of cars, print the statement.
elif trucks < cars:
    print("Maybe we couuld take the trucks.")
# If the value of trucks isn't greater than or less than that of cars, print the statement.
else: 
    print("We still can't decide.")

# If the value of people is greater than that of trucks, print the statement. 
if people > trucks:
    print("Alright, let's just take the trucks.")
# Otherwise, print the statement in else-block.
else:
    print("Fine, let's stay home then.")

# If cars more than people or more than trucks, or more than both, is True, print the statement.
if cars > people or trucks < cars: 
    print("Cars more than peple or trucks.")

# NOTES:

# If multiple elif conditions are True, Python will only run the first block.

# Zed's answers to Study Drills 29:

# Question 1:
# What do you think the if does to the code under it?
# Answer: 
# An if-statement creates what is called a "branch" in the code. 
# It's kind of like those choose your own adventure books 
# where you are asked to turn to one page if you make one choice and 
# another if you go a different direction. The if-statement tells your script, 
# "If this Boolean expression is True, then run the code under it; otherwise, skip it."

# Question 2:
# Why does the code under the if need to be indented four spaces?
# Answer: 
# A colon at the end of a line is how you tell Python you're going to create a new "block" of code, 
# and then indenting four spaces tells Python what lines of code are in that block. 
# This is exactly the same thing you did when you made functions in the first half of the book.

# Question 3:
# What happens if it isn't indented?
# Answer:
# If it isn't indented, you'll most likely create a Python error.
# Python expects you to indent something after you end a line with a : (colon).

# Question 4:
# Can you put other Boolean expressions from Exercise 27 in the if-statement?
# Answer: 
# Try it. Yes, you can, and they can be as complex as you like, 
# although really complex things generally are bad style.

# Question 5:
# What happens if you change the initial values for people, cats, and dogs?
# Answer: 
# Because you are comparing numbers, if you change the numbers, 
# different if-statements will evaluate to True and the blocks of code under them will run. 
# Go back and put different numbers in and
# see if you can figure out in your head which blocks of code will run.