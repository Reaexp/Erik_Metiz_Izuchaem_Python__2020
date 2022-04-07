number = input('Enter any number and I will tell you if it is a multiple of 10: ')
number = int(number)

if number % 10 == 0:
    print('This number is a multiple of 10.')
else:
    print('This number is not a multiple of 10.')