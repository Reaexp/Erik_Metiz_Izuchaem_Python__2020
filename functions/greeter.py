# def greet_user():
#     """Выводит простое приветствие.""" # Текст представляет собой комментарий — \
#     # строку документации с описанием функции.
#     print("Hello, Alex!")
# greet_user()

# def greet_user(username):
#     """Выводит простое приветствие."""
#     print(f"Hello, {username.title()}!")
#
# greet_user("alex")


def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nПожалуйста, скажите свое имя и фамилию. ")
    print("Напишите 'стоп' или 'stop' что бы остановить программу")
    f_name = input("имя: ")
    if f_name == "стоп" or f_name == "stop":
        break
    l_name = input("фамилия: ")
    if f_name == "стоп" or f_name == "stop":
        break

    formated_name = get_formatted_name(f_name, l_name)
    print(f"Привет {formated_name}")
