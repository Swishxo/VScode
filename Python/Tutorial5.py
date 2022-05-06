#Lists are used to store multiple items in a single variable.

names = ["Steph", "Naruto", "Goku"]
print(names)

#List can also store different data types
data = ["hello", 2, 3.3, 'e']
print(data)

#A List is considered a data-type, its type is List
print(type(names))
print(type(data))

#List items are indexed, the first item has index [0], the second item has index [1] etc.
print(names[0])
print(names[1])
print(names[2])

#List allow for duplicate items
names[1] = "Stephon"
names[2] = "Stephon"
print(names)

#loop through a List

for x in names:
    print(x)

#insert into a list without replacing any of the existing values

data.insert(1, "Hello")
print(data)

#add an item to the end of the list

names.append("Boruto")
print(names)

#removes the last item of a List
names.pop()
print(names)

#remove an item based on index
names.pop(1)
print(names)

