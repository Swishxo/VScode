#A set is a collection which is unordered, unchangeable*, and unindexed.
    #Sets are written with curly brackets.
    #Once a set is created, you cannot change its items, but you can remove items and add new items

#Sets cannot have two items with the same value

teams ={"Nets", "Knicks", "Hornets"}
print(teams) #Sets are unordered, so you cannot be sure in which order the items will appear.

#A set can contain different data types

set1 = {"Hello", 4.5, 'i', 6, True}
print(set1)

#You cannot access items in a set by referring to an index or a key
    #you can loop through the set items using a for loop

for x in set1:
    print(x)

#Check if set has an item
print("Hello" in set1) #return true

#Once a set is created, you cannot change its items, but you can add new items

teams.add("Celtics")
print(teams)

# remove an item in a set, use the remove(), or the discard() method
    #If the item to remove does not exist, remove() will raise an error
    #If the item to remove does not exist, discard() will NOT raise an error

teams.remove("Knicks")
print(teams)

#You can also use the pop() method to remove an item, but this method will remove the last item

teams.pop()
#when using the pop() method with a set, you do not know which item that gets removed
print(teams)