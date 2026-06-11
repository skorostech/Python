#create a child class dog that inherits from animal
#create an object d1 = Dog('Rex')
#call d1.bark()
class Animal:
    def __init__(self , name):
        self.name = name
        
    def bark(self):
        print(self.name)
        
#create thedog class that inherists from Animal
class Dog(Animal):
    pass
#Create an object
d1 = Dog('Rex')
print(f'{d1.name} can bark')
#Call the bark method
d1.bark()
