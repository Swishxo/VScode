#A function is a block of code which only runs when it is called
    #A function can return data as a result

#a function is defined using the def keyword

def myFunction():
    print("We are within the function")

myFunction()

#you add arguments to functions

def userName(name):
    print("Hello user,", name)

userName("Stephon")

#you can add as many arguments as you want. You must seperate them by commas

def registerTeam(city, teamName):
    print("Your team the " + teamName + " is from " + city)

registerTeam("Brooklyn", "Nets")

#the data-type passed into the parameters do not matter

def calculations(num1, num2):
    return num1 + num2

#can pass the function data to a variable

ans = calculations(3, 2)
print(ans)

#also we can just display the results from the print function

def justAdd(x):
    return x + 10

print(justAdd(3))


