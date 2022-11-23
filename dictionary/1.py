# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# car = 'Audi'
# print(car.lower() == 'audi')
# print(car)

# car = 'Audi'
# if car != 'bmw':
#     print('Hold bmw')

# age = 18
# if age != 42:
#     print('Это неправильный ответ. Пожалуйста, попробуйте еще раз!')

# age_1 = 22
# age_2 = 18
# print(age_1 >= 21 or age_2 >= 21 )
# age_1 = 18
# print(age_1 >= 21 or age_2 >= 21 )

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
#
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

# age = 15
# if age >= 18:
#     print ('Ты уже достаточно взрослый, чтобы голосовать!')
#     print ('Вы уже зарегистрировались для голосования?')
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
#
# print("\nFinished making your pizza!")

# alien_color = 'green'
# if alien_color == 'green':
#     print('Вы заработали 5 очков')

# alien_color = 'red'
# if alien_color == 'green':
#     print('Вы заработали 5 очков')
# elif alien_color == 'yellow':
#     print('Вы заработали 10 очков')
# else:
#     print('Вы заработали 15 очков')
# age = 1
# if age <= 2:
#     print('младенец')
# if age >= 2 and age <= 4:
#     print('малыш')
# if age >= 4 and age <= 13:
#     print('ребенок')

# fruit = [1, 2, 3, 4, 5]
# if 2 in fruit:
#     print('You really like bananas!')

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.") # Извините, у нас сейчас закончился зеленый перец.
#     else:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# requested_toppings = []
# if requested_toppings :
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print('Are you sure you want a plain pizza?')

# available_toppings = ['mushrooms', 'olives', 'green peppers',
# 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for topping in requested_toppings:
#     if topping in available_toppings:
#         print(f"Adding {topping}.")
#     else:
#         print(f"Sorry, we don't have {topping}.")
# print("\nFinished making your pizza!")

# users = ['Alex', 'Tima','admin', 'Nata', 'Ang']
# if not users:
#     print('We need to ind some users!')
# else:
#      for user in users:
#          if user == 'admin':
#              print('Привет, администратор, вы хотели бы увидеть отчет о состоянии?')
#          else:
#              print(f'Hello {user.title()} , thank you for logging in again')

# current_users = ['Alex', 'Tima', 'admin', 'Nata', 'Ang']
# current_users_lower = [user.lower() for user in current_users]
# new_users = ['Lena', 'Ula', 'Dima', 'NATA', 'Ang']
# new_users_lower = [user.lower() for user in new_users]
# # print(current_users_lower)
# for user in new_users_lower:
#     if user.lower() not in current_users_lower:
#         print(f'{user.title()} - это имя доступно.')
#     else:
#         print(f'Привет {user.title()}, это имя уже занято, выбирите другое!')

numbers = list(range(1,10))
# print(numbers)
for number in numbers:
    if number == 1 in numbers:
        print(f'{number}st')
    else:
        print(f'{number}th')

print()
