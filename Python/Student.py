class User:

    def hello(self):
        print("Whats suppp!!!")


#classes and Objects
    #parenthesis on the end of a class mean inheritance
class Student(User):

#this is the constructor for python
 #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
        #self.onProbation = onProbation

#Creating a function
    def onHononors(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

#function with parmeters
    def simpleMath(self, x):
        print("The number you add will get a +5")
        return x + 5

#static function
    #can be called independently because it not tied to the class
    def classDiscription():
        print("This class repersents the students")

#method overload 
    #useful for describing class obj
    #instead of returning memory adress
    #this is a method override
    #hint: to see difference comment out method 

    #@override
    def __str__(self):
        print("Student Description as follow:")
        return self.name + " " + self.major 

#method that takes an object
    #must pass an object of type student

    def showAll(Student):
        for x in Student:
            print("yup!!!!!!!!!!!!!!")
            print(x)

#another method that useful to override
    #is the equal method

    def __eq__(self, other):
        if self.name == other.name and self.gpa == other.gpa:
            return True
        else:
            return False
        
#getter in python

    @property
    def name(self):
        print("getting name")
        return self._name

#setter

    @name.setter
    def name(self, name):
        print("setting name")
        self._name = name