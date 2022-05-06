#import your Student class
    #from (YourClassParentDir) import (Class)
from Student import Student

#create Student object
student1 = Student("Steph", "Comp sci", 3.8)
student2 = Student("Cash", "IT", 3.3)

print(student2.simpleMath(4))

#can pass obj into a list

mathDept = [Student("July", "Accontant", 3.0), 
            Student("Steph", "Comp sci", 3.8)]

#index through each student
for x in mathDept:
    print(x.onHononors())

#Change values independently 
mathDept[0].major = "Journalism"
print(mathDept[0].major)

#Calling a static method
    #You call a static method through class name

print(Student.classDiscription())

#class method override 
    #returns class attribute
    #doesnt return pointer to memory

print(mathDept[0])
print(mathDept[1])

#call obj method
Student.showAll(mathDept)

#check if equals
print(mathDept[0] == mathDept[1])

#using getter
print(mathDept[0].name)

#using inheritance from User class

mathDept[0].hello()
mathDept[1].hello()


    
