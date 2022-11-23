# magicians = ['alice', 'david', 'carolina']
# for wizard in magicians: # wizard - волшебник
#     print(f'{wizard.title()}, that was a great trick!')
#     print(f' I can\'t wait to see you next trick, {wizard.title()}\n')
#
# print('Thank you, everyone. That was a great magic show!')

# pizzas = ['сырная', 'колбасная', 'сладкая', 'острая']
# for pizza in pizzas:
#     print(f'I like {pizza.title()} pizza')
# print('\nI really love pizza!')

# for valeu in range(1,6):
#     print(valeu)

# numbers = list(range(2,110,2))
# print(numbers)

# squares = []
# for valeu in range(1,11):
#     square = valeu**2
#     squares.append(square)
# print(squares)

# squares = []
# for valeu in range(1,11):
#     squares.append(valeu**2)
# print(squares)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(sum(digits))

# squares = [value**2 for value in range(1,11)]
# print(squares)


# numbers = list(range(3,31,3))
# # for number in numbers:
# #     print(number)
# # print(sum(numbers))
# # print(max(numbers))
# print(numbers)

# cube = [valeu*3 for valeu in range(1,11)]
# print(cube)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# my_foods = ['pizza', 'falafel', 'carrot cake', 'apple']
# friends_foods = my_foods[:]
# my_foods.append('cannoli')
# friends_foods.append('ice cream')
#
# print('My favorite foods are:')
# print(my_foods)
# print('\nMy friend\'s favorite foods are:')
# print(friends_foods)
# my_foods = ['pizza', 'falafel', 'carrot cake', 'apple', 'lemon']
# print('The irst three items in the list are:')
# print(my_foods[-3:])

# pizzas = ['charles', 'martina', 'michael', 'florence', 'eli']
# friend_pizzas = pizzas[:]
# pizzas.append('1')
# friend_pizzas.append(2)
# print('My favorite pizzas are:')
# for pizza in pizzas:
#     print(pizza)
# print('My friend’s favorite pizzas are:')
# for f_pizza in friend_pizzas:
#     print(f_pizza)

# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)
# print(dimensions[0])
# print(dimensions[1])

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100, 'ewe', 'rwerw')
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
