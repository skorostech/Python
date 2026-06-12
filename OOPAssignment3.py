#Create a parent class called shape with a method area() .
# Then create two child classes , Circle and Rectangle , that override the area () method to calculate and display their respective areas
#Polynmorphism: Calling area () on different objects produces different results
class Shape:
        
    def area(self):
        print('Area of a shape')
        
#Overriding
        
class Circle(Shape):
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        area = 3.142 * self.radius * self.radius
        print('Area of a circle is' , area)
        
class Rectangle(Shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width
        
    def area(self):
        area = self.length * self.width
        print('Area of a rectangle is' , area)
     
c1 =Circle(7)
r1 = Rectangle(5 , 6)
c1.area()
r1.area()   
        
        
#Super() Function
class Animal:
    def __init__(self , name):
        self.name = name
        
class Dog(Animal):
    def __init__(self , name , age):
        #Calls the parents constructor
        super(). __init__(name)
        self.age = age
        
d1 = Dog('Rex' , 2)
print(d1.name , 'is' , d1.age , 'years old')

class Animal:
    def __init__(self , name):
        self.name = name
        
    def speak(self):
        print(self.name , 'can bark')
        
class Dog(Animal):
    def speak (self):
        super(). speak()
        print(self.name , 'can Woof!')
        
d1 = Dog('Rex')
d1.speak()
       