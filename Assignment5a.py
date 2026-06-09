#create a function to print all the odd numbers from 5 to 20
def odd_numbers():
    for i in range(5 , 21):
        if i % 2 != 0:
            print('The odd number is: ', i)
odd_numbers()