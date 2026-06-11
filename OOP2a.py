class Dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
dog1 = Dog('Buddy' , 3)
print('This dog is called' , dog1.name , 'it is' , dog1.age , 'years old')