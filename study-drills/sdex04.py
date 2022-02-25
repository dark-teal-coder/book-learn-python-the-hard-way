# Study Drills 04

# Traceback (most recent call last):
# File "ex4.py", line 8, in <module>
# average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
# Explain this error in your own words. Make sure you use line numbers and explain why.
# Here's more Study Drills:
# 1. I used 4.0 for space_in_a_car, but is that necessary? 
# What happens if it's just 4?
# 2. Remember that 4.0 is a floating point number. 
# It’s just a number with a decimal point, and 
# you need 4.0 instead of just 4 so that it is floating point.
# 3. Write comments above each of the variable assignments.
# 4. Make sure you know what = is called (equals) and 
# that its purpose is to give data (numbers, strings, etc.) names (cars_driven, passengers).
# 5. Remember that _ is an underscore character.
# 6. Try running python3.6 as a calculator like you did before and 
# use variable names to do your calculations. 
# Popular variable names are also i, x, and j.

# If we use 4, the result will be an integer. 
# If we use 4.0, the result will be a float. 
print(30 * 4.0, 30 * 4)

# Reason of the error: car_pool_capacity is different from carpool_capacity

# Assign the integer 100 to the variable cars.
cars = 100
# Assign the floating point number 4.0 to the variable space_in_a_car. 
space_in_a_car = 4.0
# Assign the integer 30 to the variable drivers.
drivers = 30
# Assign the integer 90 to the variable passengers.
passengers = 90
# Evaluate the expression on the right. 
# Take the value cars refers to.
# Minus it by the value drivers refers to.
# Assign the calculation result to the variable cars_not_driven. 
cars_not_driven = cars - drivers
# Assign the value drivers refers to to the variable cars_driven. 
cars_driven = drivers
# Evaluate the expression on the right.
# Take the value cars_driven refers to.
# Multiply it by the value space_in_a_car refers to. 
# Assign the calculation result to the variable carpool_capacity. 
carpool_capacity = cars_driven * space_in_a_car
# Take the value passengers refers to.
# Divide it by the value cars_driven refers to. 
# Assign the calculation result to the variable average_passengers_per_car. 
average_passengers_per_car = passengers / cars_driven