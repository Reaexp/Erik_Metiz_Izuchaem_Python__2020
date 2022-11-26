# def get_formated_name(first_name, last_name):
#     """Возвращает аккуратно отформатированное имя."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_formated_name("алекс", "reaexp")
# print(musician)


# def get_formated_name(first_name, middle_name, last_name):
#     """Возвращает аккуратно отформатированное полное имя."""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formated_name("алекс", "крутой", "reaexp")
# print(musician)

# def get_formated_name(first_name, last_name, middle_name=''):
#     """Возвращает аккуратно отформатированное полное имя."""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formated_name("алекс", "reaexp")
# print(musician)
#
# musician = get_formated_name("алекс", "крутой", "reaexp")
# print(musician)


def build_person(first_name, last_name):
    """Возвращает словарь с информацией о человеке."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('алекс', 'reaexp')
print(musician)


# def build_person(first_name, last_name, age = None):
#     """Возвращает словарь с информацией о человеке."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
# musician = build_person('алекс', 'reaexp', age = 35 )
# print(musician)