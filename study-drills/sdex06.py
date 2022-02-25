# Study Drills 06

# 1. Go through this program and write a comment above each line explaining it.
# 2. Find all the places where a string is put inside a string. There are four places.
# 3. Are you sure there are only four places? How do you know? Maybe I like lying.
# 4. Explain why adding the two strings w and e with + makes a longer string.

# Assign 10 to the variable types_of_people. 
types_of_people = 10
# f marks the string to be formatted - f-string. 
# An f-string has {} containing expressions to be replaced with their values at runtime. 
# Embed the variable types_of_people in the string.
# Replace the value of the variable in the {} placeholder when used. 
# Assign the string to be formatted to the variable x. 
x = f"There are {types_of_people} types of people."

# # Take 10 in format() and put it in the position {0:d} as decimal integer. 
# # And assign the string to the variable x. 
# x = "There are {0:d} types of people.".format(10)

# Assign "binary" to the variable binary. 
binary = "binary"
# Assign "don't" to the variable do_not.
do_not = "don't"

# Embed the variables binary and do_not in the string. 
# Replace the value of the variable in the {} placeholder when used.
# Assign the string to be formatted to the variable y. 
y = f"Those who know {binary} and those who {do_not}."

# # Take the variables binary and do_not and put them in to replace {0:s} and {1:s} with their values as string.
# # Assign the string to the variable y. 
# y = "Those who know {0:s} and those who {1:s}.".format(binary, do_not)

# Evaluate the expression in the replacement field {types_of_people}. 
# Print the value in x. 
print(x)
# Evaluate the expression in the replacement fields {binary} and {do_not}. 
# Print the value in y. 
print(y)

# Put the formatted string the variable x refers to in the {}. 
# Mark the string with f as there is a variable in {}. 
print(f"I said: {x}")
# Put the formatted string the variable y refers to in the {}. 
# Mark the string with f as there is a variable in {}. 
print(f"I also said: '{y}'")

# # Take the variable x and put it in to replace {0!r} with its value as "official" string object representation.
# print("I said: {0!r}.".format(x))
# # Take the variable y and put it in to replace {0:s} with its value as string. 
# print("I also said: '{0:s}'.".format(y))

# Assign the value False to the variable hilarious.
hilarious = False
# Assign a string containing a {} placeholder to the variable joke_evaluation. 
joke_evaluation = "Isn't that joke so funny?! {}"

# # Assign the string with {0!r} placeholder in it to the variable joke_evaluation. 
# # !r - convert the value to a string using repr().
# joke_evaluation = "Isn't that joke so funny?! {0!r}"

# Take the value the variable hilarious refers to.
# Put it in to replace {} in the string the variable joke_evaluation refers to. 
print(joke_evaluation.format(hilarious))

# # Take the value the variable hilarious refers to.
# # Put it in to replace {0!r} in the string the variable joke_evaluation refers to. 
# print(joke_evaluation.format(hilarious))

# Assign the string "This is the left side of..." to the variable w. 
w = "This is the left side of..."
# Assign the string "a string with a right side." to the variable e. 
e = "a string with a right side."

# Concatenate the strings w and e represent and print the concatenated string. 
print(w + e)

# Places where a string is inside a string:
# Line 29: y = f"Those who know {binary} and those who {do_not}."
# Line 44: print(f"I said: {x}")
# Line 47: print(f"I also said: '{y}'")