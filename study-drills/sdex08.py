# Study Drills 08

# Do your checks, write down your mistakes, 
# and try not to make the same mistakes on the next exercise.
# In other words, repeat the Study Drills from Exercise 7.

# Create a string with 4 placeholders {}, {}, {} and {} with spaces between them.
# Assign it to the variable formatter. 
formatter = "{} {} {} {}"
# Create a string with 4 placeholders {0!r}, {1!r}, {2!r} and {3!r} with spaces between them.
# Assign it to the variable formatter. 
# r% in Python 2 or !r in Python 3 is "raw" format for debugging.
# formatter = "{0!r} {1!r} {2!r} {3!r}"

# Take the numbers 1, 2, 3 and 4 and replace the placeholders with them, respectively. 
print(formatter.format(1, 2, 3, 4))
# Take the strings "one", "two", "three" and "four" and replace the placeholders with them, respectively. 
print(formatter.format("one", "two", "three", "four"))
# Take the Boolean values True, False, False and True and replace the placeholders with them, respectively. 
print(formatter.format(True, False, False, True))
# Take the formatter and replace all the placeholders with it, respectively. 
print(formatter.format(formatter, formatter, formatter, formatter))
# Take the sentence strings and replace the placeholders with them, respectively. 
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear")
)