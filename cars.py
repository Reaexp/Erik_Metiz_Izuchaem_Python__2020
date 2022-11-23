# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# car = 'Audi'
# print(car.lower() == 'audi')
# print(car)
#
# Jonn jonn

# requested_toppings = 'mushrooms'
# if requested_toppings != 'anchovies':
#     print('Hold the anchovies')

# age = 18
# print(age == 18)

# answer = 16
# if answer <= 42:
#     print('That is not the correct answer. Please try again!')

# age_0 = 22
# age_1 = 18
# print(age_0 <= 21 or age_1 >=21)

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_toppings)
# print('pepperoni' in requested_toppings)

# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
# if user not in banned_users:
#     print(f'{user.title()}, you can post a response if you wish.')

# game_active = True
# can_edit = False

# age = 19
# if age >= 18:
#     print('You are old enough to votel!')
#     print('You are old enough to votel!')
# else:
#     print('Sorry, you are too young to voite.')

# age = 2
# if age < 4:
#     print('Your admission cost is 0$')
# elif age < 18:
#     print('Your admission cost is 25$')
# else:
#     print('Your admission cost is 40$')

# age = 6346346
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40
# print(f'Your admission cost is {price} $')

age = 60
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
# else:
#     price = 20
print(f'Your admission cost is {price} $')

# requested_toppings = ['mushrooms', 'extra cheese']
#
# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms')
# elif 'pepperoni' in requested_toppings:
#     print('Adding pepperoni')
# elif 'extra cheese' in requested_toppings:
#     print('Adding extra cheese')
# print('\nFinished making your pizza!')

# requested_toppings = ['mushrooms', 'green peppers','extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('Sorry, we are out of green peppers right now!')
#     else:
#         print(f'Adding {requested_topping}.')
# print('\nFinished making your pizza!')

# requested_toppings = ['mushrooms', 'green peppers','extra cheese']
#
# if requested_toppings :
#     for requested_topping in requested_toppings:
#         print(f'Adding {requested_topping}.')
#     print('\nFinished making your pizza!')
# else:
#     print('Are you sure want a plain pizza?')

availible_toppings = ['mushrooms', 'olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms', 'friench fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availible_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f'Sorry, we dont have {requested_topping}.')
print('\nFinished making your pizza!')
