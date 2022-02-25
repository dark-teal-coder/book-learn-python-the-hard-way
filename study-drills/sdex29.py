# Study Drills 29

# In this Study Drill, try to guess what you think the if-statement is and what it does. 
# Try to answer these questions in your own words before moving on to the next exercise:
# 1. What do you think the if does to the code under it?
# 2. Why does the code under the if need to be indented four spaces?
# 3. What happens if it isn't indented?
# 4. Can you put other Boolean expressions from Exercise 27 in the if-statement? Try it.
# 5. What happens if you change the initial values for people, cats, and dogs?

people = 20
cats = 30
dogs = 15

if people < cats:
# if True:
    print("Too many cats! The world is doomed!")

if people > cats:
# if False: 
    print("Not many cats! The world is saved!")

if people < dogs:
# if False:
    print("The world is drooled on!")

if people > dogs:
# if True: 
    print("The world is dry!")

dogs += 5 # dogs is now 20.

if people >= dogs:
# if (people > dogs) or (people == dogs):
# if False or True: 
# if True: 
    print("People are greater than or equal to dogs.")

if people <= dogs:
# if (people < dogs) or (people == dogs):
# if False or True: 
# if True:
    print("People are less than or equal to dogs.")

if people == dogs:
# if True:
    print("People are dogs.")

# MY ANSWERS:
# 1. The if-statement evaluates the condition. 
# If true, it'll execute the statements under it.
# 2. To tell Python that these indented statements will only be executed when the condition is met.
# 3. When no or wrong indentation under if, IndentationError occurs. 
# 5. The conditions will result in different Boolean values. 
# Different print statements may be executed.