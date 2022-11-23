# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edvard': 'ruby',
#     'phil': 'python',
#     }
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# for name, language in favorite_languages.items():
#     print(f"\nKey: {name}")
#     print(f"Value: {language}")

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")
#
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our pool!")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for talking the pool.")


# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())


# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edvard': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:
        print(f"\t{language.title()}")