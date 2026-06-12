class Animal:
    def __init__(self , name):
        self.name = name
        
    def speak(self):
        print(self.name , 'can bark')
        
class Dog(Animal):
    
    def speak(self):
        print('Woof!!')
        
d1 = Dog('Rex')
d1.speak()