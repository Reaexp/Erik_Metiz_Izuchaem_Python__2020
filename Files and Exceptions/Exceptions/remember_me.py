import json

# user_name = input("What is your name? ")
#
# filename = 'username.json'
# with open(filename, 'w') as f:
#     json.dump(user_name.title(), f)
#     print(f"We'll remember you when you come back, {user_name.title()}")


# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
# filename = 'username.json'
# try:
#     with open(filename) as f:
#         username = json.load(f)
# except FileNotFoundError:
#     username = input("What is your name? ")
#     with open(filename, 'w') as f:
#         json.dump(username, f)
#         print(f"We'll remember you when you come back, {username.title()}")
#
# else:
#     print(f"Welcome back, {username}")

def sorted_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def new_username():
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username.title(), f)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    name = input("Введите свое имя: ")
    username = sorted_username()
    if name.title() == username:
        print(f"Welcome back, {username}")

        username = new_username()
        print(f"We'll remember you when you come back, {username.title()}")
    else:
        print('неправильное имя! Попробуйте ещё раз!')

greet_user()