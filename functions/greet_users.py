def greet_users(names):
    """Вывод приветствия для каждого пользователя функции."""
    for name in names:
        message = f"Привет, {name.title()}!"
        print(message)

user_name = ["алекс", "тим", "дим"]
greet_users(user_name)