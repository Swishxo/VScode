#Dictionaries are used to store data values in key:value pairs.
    #A dictionary is a collection which is ordered*
    #changeable and do not allow duplicates

#Dictionaries are written with curly brackets
cars = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1999,
    #The values in dictionary items can be of any data type
    #String, int, boolean, and list data types
    "colors": ["red", "white", "blue"]
}

print(cars)

#Dictionary items are presented in key:value pairs, and can be referred to by using the key name
print(cars["model"])

#dictionaries are ordered, it means that the items have a defined order
    #and that order will not change


#Accessing Items
#You can access the items of a dictionary by referring to its key name
carBrand = cars["brand"]
print(carBrand)

#There is also a method called get() that will give you the same result
modelYear = cars.get("year")
print(modelYear)

#Get Keys
#The keys() method will return a list of all the keys in the dictionary

carKeys = cars.keys()
print("Here are the keys: ", carKeys)

#add to dict

cars["version"] = 1.0
print(cars.get("version"))

#The values() method will return a list of all the values in the dictionary
dictValues = cars.values()
print(dictValues)

