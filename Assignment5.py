#write a function to print the even numbers from 1 to n
def even_numbers(n):
    for i in range(1 , n + 1):
        if i % 2 == 0:
            print('The even number is: ', i)
even_numbers(20)