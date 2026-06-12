#Encapsulation
#Hiding data and controlling access to it
class Student:
    def __init__(self , name):
        #The double underscore __ makes the variable private.
        self.__name = name
        
    def display(self):
        #The name is hidden inside the class and accessed through a method.
        print(self.__name)
        
s1 = Student('John')
s1.display()