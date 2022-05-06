#A for loop is used for iterating over a sequence
    #that is either a list, a tuple, a dictionary, a set, or a string

fruits = ["apple", "banana", "cherry"]

#The for loop does not require an indexing variable to set beforehand.
for i in fruits:
    print(i)

#range() Function loop through a set of code a specified number of times
for x in range(6):
  print(x)

#nested loop, "inner loop" will be executed one time for each iteration of the "outer loop"

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

