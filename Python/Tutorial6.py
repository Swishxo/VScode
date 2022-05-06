#Tuples are used to store multiple items in a single variable
    #A tuple is a collection which is ordered and UNCHANGABLE
    #Tuples are written with round brackets  

games = ("Halo", "Sonic", "COD")
print(games)

#Tuple items are indexed, the first item has index [0]
print(games[0])
print(games[1])
print(games[2])

#A Tuple can have mixed data-types
mixed = ("hello", 9, '4', 8.7)
print(mixed)

#Tuples are defined as tuple
print(type(games))
print(type(mixed))

#looping through a tuple

for x in games:
    print(x)

#Change Tuple value
'''
Once a tuple is created, you cannot change its values. Tuples are unchangeable.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
'''

names = ("BMW", "Corvette", "Tesla")
print(names)
conversion = list(names) #cast names as a list
#now we make changes
conversion[2] = "Rivian"
#now convert list back to tuple
names = tuple(conversion)

print(names)

#Tuples only have two methods
    #count()
    #index()

#Inorder for any changes to be done to the tuple it must be converted to a List
    #once it is converted it can utiliza all methods from List
    #then convert the List back to a Tuple once changes are done


