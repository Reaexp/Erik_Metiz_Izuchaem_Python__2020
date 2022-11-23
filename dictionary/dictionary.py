# alien_0 = {'color': 'green', 'points': '5'}
# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color': 'green', 'points': '5'}
# new_points = alien_0['points']
# print(f'You just earned {new_points} points!')

# alien_0 = {'color': 'green', 'points': '5'}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
# print(alien_0)
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}")
#
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}")

# alien_0 = {'x_position': 0, 'y_position': '25', 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")
# # Пришелец перемещается вправо.
# # Вычисляем величину смещения на основании текущей скорости.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# elif alien_0['speed'] == 'fast':
#     x_increment = 3
# # else:
# #     # пришелец двигается быстро
# #     x_increment = 3
# # Новая позиция равна сумме старой позиции и приращения.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

# alien_0 = {'color': 'green', 'points': '5'}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
#
# language = favorite_languages['sarah'].title()
# print(f" Sarah's favorite language is {language}.")
# print(favorite_languages['sarah'].title())

# alien_0 = {'color': 'green', 'speed': 'slow'}
# points_value = alien_0.get('points', 'No points value assigned.')
# print(points_value)

# list_1 = {
#     'first_name': 'Alex',
#     'last_name': 'Leontev',
#     'age': '36',
#     'sity': 'moscow',
# }
#
# # print(list_1['first_name'])
# # print(list_1['last_name'])
# # print(list_1['age'])
# # print(list_1['sity'])
#
# for key, valeu in list_1.items():
#     # print(key.upper())
#     # print(valeu.title())
#     # print('\n')
#     print(f'Key : {key}')
#     print(f'Value : {valeu}\n')

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# # for name, language in favorite_languages.items():
# #     print(f"{name.title()}'s favorite language is {language.title()}.")
#
# for name in favorite_languages.keys():
#     print(name.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# friends = ['phil','sarah']
# for name in favorite_languages.keys():
#     print(f'Hi {name.title()}')
#
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if name not in friends:
#     continue
# language = favorite_languages[name].title()
# print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking thr pool!")

# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# favorite_languages = {
#     'jen': '+',
#     'sarah': '+',
#     'edward': '+',
#     'phil': '+',
# }
#
# favorite_languages['alex'] = '+'
# favorite_languages['nata'] = '-'
# favorite_languages['tima'] = '-'
#
# for name, value in favorite_languages.items():
#     if value == '+' in favorite_languages:
#         print(f"{name.title()}, Спасибо за опрос!")
#     else:
#         print(f"{name.title()}, Пройдите участие в опросе!")

# spisok = {'alex', 'nata', 'tima', 'dima', 'lina', 'ula' }
# new = {'alex', 'nata', 'tima'}
#
# for name in sorted(spisok):
#     if name in new:
#         print(f"{name.title()} - спасибо что пришли!")
#     else:
#         print(f"{name.title()} - примите участие в мероприятии!")

# alien_0 = {'color': 'green', 'points': '5'}
# alien_1 = {'color': 'yellow', 'points': '10'}
# alien_2 = {'color': 'red', 'points': '15'}
#
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)
#
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
#     aliens.append(new_alien)
#
#     for alien in aliens[0:3]:
#         if alien['color'] == 'green':
#             alien['color'] = 'yellow'
#             alien['speed'] = 'medium'
#             alien['points'] = '10'
#         elif alien['color'] == 'yellow':
#             alien['color'] = 'red'
#             alien['speed'] = 'fast'
#             alien['points'] = '15'
#
#
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f"Total number of aliens: {len(aliens)}")

# spisok = [-3, 0, 2, 4, 5]   # k = 6
# spisok_2 = []
# for a in spisok:
#     spisok[0:5] = spisok_2.append()
#
# print(spisok_2)

# pizza = {
#     'crust': 'trick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }
# print(f"You ordered a {pizza['crust']} - crust pizza "
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': 'c',
#     'edward': ['ruby','go'],
#     'phil': ['python', 'ruby'],
#     }
# for name, languages in favorite_languages.items():
#     if len(languages) == 1:
#         print(f"{name.title()}'s favorite language is: ")
#     else:
#         print(f"{name.title()}'s favorite language are: ")
#     for language in languages:
#         print(f"\t{language.title()}")

# users = {
#     'aeinstein' : {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#         },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'einstein',
#         'location': 'princeton',
#         },
# }
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tlocation: {location.title()}")


people = {
    'husband': {
        'first_name': 'leontev',
        'last_name': 'aleksey',
        'age': '36',
        'city': 'schelkovo'
        },
    'wife': {
        'first_name': 'leonteva',
        'last_name': 'natalia',
        'age': '25',
        'city': 'schelkovo'
        },
    'son': {
        'first_name': 'leontev',
        'last_name': 'tima',
        'age': '11',
        'city': 'schelkovo'
        },
    'friend':{
        'first_name': 'gebert',
        'last_name': 'eduard',
        'age': '43',
        'city': 'egorevsk'
        },
}
for key, value in people.items():
    print(f"{key.upper()}")
    full_name = f"{value['first_name'].title()} {value['last_name'].title()} - {value['age']}"
    location = f"{value['city'].title()}"
    print(f"\tFull name : {full_name}")
    print(f"\tCity : {location}")