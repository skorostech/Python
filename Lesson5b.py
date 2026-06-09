#functions with parameters
def greet(name) :
    print('Good morning' , name)
    greet('Sylvia')
    
def addition(num1 , num2):
    sum = num1 + num2
    print('The sum is' , sum)
    addition(20 , 30)
    
#subtraction
def subtraction(num1 , num2):
    sub = num1 - num2
    print('The difference is' , sub)
    subtraction(30 , 20)
    
#multiplication
def multiplication(num1 , num2):
    mult = num1 * num2
    print('The product is' , mult)
    multiplication(20 , 10)
    
#division
def division(num1 , num2):
    div = num1 / num2
    print('The quotient is' , div)
    division(20 , 10)
    
#modulus
def modulus(num1 , num2):
    mod = num1 % num2
    print('The modulus is' , mod)
    modulus(20 , 10)
    
#simple interest
def simple_interest(principal , rate , time):
    si = (principal * rate * time) / 100
    print('The simple interest is' , si)
    simple_interest(20 , 10 , 2)
    
#BMI
def bmi(weight , height):
    result = weight / (height * height)
    print('BMI is' , result)
    bmi(70 , 1.75)
    