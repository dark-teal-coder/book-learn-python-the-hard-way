# Study Drills 34

# 1. With what you know of the difference between these types of numbers, 
# can you explain why the year 2010 in "January 1, 2010," really is 2010 and not 2009? 
# (Hint: you can't pick years at random.)
# 2. Write some more lists and work out similar indexes until you can translate them.
# 3. Use Python to check your answers.

# MY ANSWER:
# 1. Assuming there are 365 days in a year. 
# From day 1 to day 365, it's the 1st year or in year 0001. 
# January 1, 0001 to December 31, 0001 are year 1.
# Thus, January 1, 2010 is year 2010. 

numbers = [1, 2, 3, 4, 5]
people = ["person1", "person2", "person3", "person4", "person5"]

for num in numbers:
    print("Index:", numbers.index(num))
    print(num)

for person in people:
    print("Index:", people.index(person))
    print(person)