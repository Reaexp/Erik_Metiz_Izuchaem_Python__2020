# alien_0 = {'color': 'green', 'points': 5}
#
# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
# print(alien_0)
#
# alien_0['color'] = 'green'
# alien_0['points'] = 5
#
# print(alien_0)

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
#
# alien_0 ['color'] = 'yelow'
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")
# alien_0['speed'] = 'fast'
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)


# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_valeu = alien_0.get('points', 'No point value assigned.')
# print(point_valeu)


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5,'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print('...')
# print(f"Total number of aliens: {len(aliens)}")


# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5,'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = '10'
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = '15'
#
# for alien in aliens[:5]:
#     print(alien)
# print('...')


favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edvard': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) <= 1 in favorite_languages:
        print(f"\n{name.title()}'s favorite language is {language.title()} ")
    else:
        print(f"\n{name.title()}'s favorite languages are: {languages} ")
        for language in languages:
            print(f"\t{language.title()}")