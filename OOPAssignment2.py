class Calculator:
    def __init__(self, num1 , num2):
        self.num1 = num1
        self.num2 = num2
      
    def add(self) :
        print (f'The sum is' , c1.num1 + c1.num2)
        
    def subtract(self) :
        print ('The subtraction is' , self.num1 - self.num2)
        
    def multiply(self) :
        print('The multiplication is' , self.num1 * self.num2)
        
    def divide(self) :
        print('The division is' , self.num1 / self.num2)
       
c1 = Calculator(2 , 4)
c1.add()
c1.subtract()
c1.multiply()
c1.divide()


class Student:
    def __init__(self, name , grade ):
        self.name = name
        self.grade = grade
s1 = Student('Anna' , 'A')
print(s1.name , 'scored an' , s1.grade)
s1.name = 'Anna'
s1.grade = 'B'
print('The new grade for' , s1.name , 'is' , s1.grade)