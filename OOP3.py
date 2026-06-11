class Student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def read(self):
        print(f"{self.name} can read")
    
    def eat(self):
        print(f"{self.name}can eat because he is {self.age} years old")
    
    def sleep(self):
        print(self.name, 'is asleep')

s1 = Student('John', 20, 'john@gmail.com')
s1.read()
s1.eat()
s1.sleep()



class Car:
    def __init__(self , model , yop , color ,) :
        self.model = model
        self.yop = yop
        self.color = color
        
    def hoot(self) :
        print(c1.model , 'can hoot')
        
    def playmusic(self):
        print(c1.model , 'plays loud music')
        
    def move(self):
        print(c1.model , 'is fast')
        
c1 = Car('Toyota' , 1970 , 'blue')

c1.hoot()
c1.playmusic()
c1.move()