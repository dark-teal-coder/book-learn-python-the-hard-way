# Study Drills 19

# 1. Go back through the script and type a comment above each line explaining in English what it does.
# 2. Start at the bottom and read each line backward, saying all the important characters.
# 3. Write at least one more function of your own design, and run it 10 different ways.

# Define a function with the name cheese_and_crackers.
# Create two argument slots called cheese_count and boxes_of_crackers.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print an f-string with an embeded variable cheese_count.
    print(f"You have {cheese_count} cheeses!")
    # Print an f-string with an embeded variable boxes_of_crackers.
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Print a string. 
    print("Man that's enough for a party!")
    # Print a string. 
    print("Get a blanket.\n")

# Different ways to give the function the values it needs: 

# Print a string. 
print("We can just give the function numbers directly:")

# Call the function cheese_and_crackers and pass 2 number arguments to it.
cheese_and_crackers(20, 30)

# Print a string. 
print("OR, we can use variables from our script:")
# Assign 10 to the variable amount_of_cheese. 
amount_of_cheese = 10
# Assign 50 to the variable amount_of_crackers. 
amount_of_crackers = 50

# The variables in your function are not connected to the variables in your script.
# Call the function cheese_and_crackers and pass 2 variable arguments to it.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print a string. 
print("We can even do math inside too:")
# Call the function cheese_and_crackers.
# Evaluate the Math expressions in the argument slots before.
# Pass the resulted values to the function.
cheese_and_crackers(10 + 20, 5 + 6)

# Print a string. 
print("And we can combine the two, variables and math:")
# Call the function cheese_and_crackers.
# Take the values the variables amount_of_cheese and amount_of_crackers refer to.
# Evaluate the Math expressions in the argument slots before.
# Pass the resulted values to the function.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# My own function: 

def sum(*args):
    argsList = list(args)
    sum = 0
    for arg in argsList:
        argsList.insert(argsList.index(arg), arg)
        del argsList[argsList.index(arg) + 1]
    for num in argsList:
        sum += num
    # print(sum)
    return sum

num1 = 4
num2 = 1
print(sum(1, 2))
print(sum(1, 2, 3))
print(sum(1, 2 + 3))
print(sum(1 + 2, 3 + 4))
print(sum(num1, num2))
print(sum(1, num1 + 2))
print(sum(1, 2 + 3, num1))
print(sum(1, sum(2, 4)))
print(sum(sum(1, 4), sum(2, 4)))
print(sum(1, 2 + 3, num1, num1 + num2, sum(2, 4, num1)))