# def greet_user():
#     """Выводит простое приветствие.""" # Текст представляет собой комментарий — \
#     # строку документации с описанием функции.
#     print("Hello, Alex!")
# greet_user()

def greet_user(username):
    """Выводит простое приветствие."""
    print(f"Hello, {username.title()}!")

greet_user("alex")