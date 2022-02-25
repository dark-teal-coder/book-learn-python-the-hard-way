# Study Drills 32

# 1. Take a look at how you used range. Look up the range function to understand it.
# 2. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements?
# 3. Find the Python documentation on lists and read about them. 
# What other operations can you do to lists besides append?

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
# Mixed list:
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# The variable number is defined by the for-loop when it starts, 
# The for-loop initializes the variable to the current element of the loop iteration each time through.
# The variable number takes item #1 in the list when it goes through the loop the 1st time. 
# The variable number takes item #N in the list when it goes through the loop the Nth time. 
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# Notice we have to use {} since we don't know what's in it. 
for i in change:
    print(f"I got {i}")

# Building lists starting with an empty one
elements = []

# Then, use the range() function to do 0 to 5 (excluding 6) counts.
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append() simply appends to the end of the list.
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")

# MY ANSWER:
# 1. range(start, stop, step) function: 
    # The range() function returns a sequence of numbers and ends at a specified number after increments.
    # start: An integer number specifying at which position to start. Default is 0.
    # stop: An integer number specifying at which position to end. 
    # step: An integer number specifying the incrementation. Default is 1. 
    # range(0, N): 0, 1, 2, ..., (N-1)
# 2. Use extend() to assign range(0, 6) directly to the list: elements.extend(range(0, 6))
    # The list becomes [0, 1, 2, 3, 4, 5]. 
    # append() only adds one single item to the end of the list. 
    # elements.append(range(0, 6)) adds the whole object range(0, 6) to the list.
    # The list becomes [range(0, 6)]. 
# 3. Common list methods (https://docs.python.org/3/tutorial/datastructures.html):
    # list.append(item) adds a single item to the end of the list. 
    # list.extend(iterable) extends the list by appending all the items from the iterable to the end of the list. 
    # list.insert(index, item) inserts the item at the given index, shifting items to the right.
    # list.index(item) searches for the given item from the start of the list and returns its index. 
    # list.remove(item) searches for the first instance of the given item and removes it.
    # list.sort() sorts the list in place (does not return it). 
    # list.reverse() reverses the items of the list in place (does not return it). 
    # list.pop(index) removes and returns the item at the given index.
    # list.clear() removes all items from the list.
    # list.index(x) returns 0-based index in the list of the first item whose value is equal to x. 
    # list.count(x) returns the number of times x appears in the list.
    # del list1[n] removes an item from a list given its index n.
    # del list1[m:n] removes a slice from a list from m to (n-1). 
    # del list1[:] clears the entire list (resulting in an empty list). 
    # del list1 deletes the entire list variable (referencing the name list1 no longer available). 

# NOTES:
# 2D list: e.g. [[1, 2, 3], [4, 5, 6]]
# Using Lists as Stacks: 
    # >>> stack = [1, 2, 3]
    # >>> stack.append(4)
    # >>> stack.append(5)
    # >>> stack
    # [1, 2, 3, 4, 5]
    # >>> stack.pop()
    # 5
    # >>> stack
    # [1, 2, 3, 4]
    # >>> stack.pop()
    # 4
    # >>> stack
    # [1, 2, 3]
# Using Lists as Queues: 
    # >>> from collections import deque
    # >>> queue = deque(["person1", "person2", "person3"])
    # >>> queue.append("person4")
    # >>> queue
    # deque(['person1', 'person2', 'person3', 'person4'])
    # >>> queue.append("person5")
    # >>> queue
    # deque(['person1', 'person2', 'person3', 'person4', 'person5'])
    # >>> queue.popleft()
    # 'person1'
    # >>> queue
    # deque(['person2', 'person3', 'person4', 'person5'])
    # >>> queue.pop()
    # 'person5'
    # >>> queue
    # deque(['person2', 'person3', 'person4'])