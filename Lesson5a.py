#functions
def greet ():
    print('Good morning')
    greet()
    #a function to add two numbers
    
def add():
    num1 = 2
    num2 = 4
    sum = num1 + num2
    print('The sum is' , sum)
add()
def subtraction():
    num1 = 20
    num2 = 10
    sub = num1 - num2
    print('The difference is' , sub)
subtraction()
#multiplication
def multiply():
    num1 = 20
    num2 = 10
    mult = num1 * num2
    print('the product is' , mult)
    multiply()
    
#division
def divide():
    num1 = 20
    num2 = 10
    div = num1 / num2
    print('The quotient is' , div)
    divide()
    
#modulus
def modulus ():
    num1 = 20
    num2 = 10
    mod = num1 % num2
    print('The modulus is' , mod)
    modulus()

#simple interest
def simple_interest():
    principal = 20
    rate = 10
    time = 2
    si = (principal * rate * time) / 100
    print('The simple interest is' , si)
    simple_interest()
    
# BMI
def bmi():
    weight = 70
    height = 1.75
    result = weight / (height * height)
    print('BMI is' , result)
    bmi()