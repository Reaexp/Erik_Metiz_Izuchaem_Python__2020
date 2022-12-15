# 9.1.
# class Restaurant():
#     """Класс ресторана."""
#
#     def __init__(self, restaurant_name, cuisine_type ):
#         """Инициализирует атрибуты restaurant_name и cuisine_type."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name.title()},- {self.cuisine_type}.")
#
#     def open_restaurant(self):
#         print(f"ресторан {self.restaurant_name.title()},- открыт.")
#
#
# description = Restaurant("москва", "русская кухня")
# description.describe_restaurant()
# description.open_restaurant()

# 9.3.
# class User():
#     """Класс ресторана."""
#
#     def __init__(self, first_name, last_name, gender, age):
#         """Инициализирует атрибуты restaurant_name и cuisine_type."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.gender = gender
#         self.age = age
#
#     def describe_user(self):
#         print(f"{self.first_name.title()}, {self.last_name.title()}; {self.gender}, {self.age}.")
#
#     def greet_user(self):
#         print(f"Рады приветствовать вас {self.first_name.title()} на нашем сайте.")
#
#
# user_1 = User("alex", "reaexp", "male", 24)
# user_1.describe_user()
# user_1.greet_user()


# 9.4.
# class Restaurant():
#     """Класс ресторана."""
#
#     def __init__(self, restaurant_name, cuisine_type ):
#         """Инициализирует атрибуты restaurant_name и cuisine_type."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name.title()},- {self.cuisine_type}.")
#
#     def open_restaurant(self):
#         print(f"ресторан {self.restaurant_name.title()},- открыт.\n"
#               f"Количество обслуженных посетителей - {self.number_served}")
#
#     def restaurant(self, number):
#         self.number_served = number
#         print(f" Number is now - {self.number_served}")
#
#     def set_number_served(salf, quantity):
#         salf.number_served += quantity
#
#
#
# description = Restaurant("москва", "русская кухня")
# description.describe_restaurant()
# description.restaurant(5)
# description.open_restaurant()
#
# description.set_number_served(1)
# description.open_restaurant()
#
# description.set_number_served(6)
# description.open_restaurant()


# 9.5.
# class User():
#     """Класс ресторана."""
#
#     def __init__(self, first_name, last_name, gender, age):
#         """Инициализирует атрибуты restaurant_name и cuisine_type."""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.gender = gender
#         self.age = age
#         self.login_attempts = 0
#
#     def describe_user(self):
#         print(f"{self.first_name.title()}, {self.last_name.title()}; {self.gender}, {self.age}.")
#
#     def greet_user(self):
#         print(f"Рады приветствовать вас {self.first_name.title()} на нашем сайте.")
#
#     def increment_login_attempts(self, increase):
#         self.login_attempts += increase
#
#     def number_users_system(self):
#         print(f"Число пользователей в системе = {self.login_attempts}")
#
#     def reset_login_attempts(self, null):
#         if null == 0:
#             self.login_attempts = 0
#
#
# user_1 = User("alex", "reaexp", "male", 24)
# user_1.describe_user()
# user_1.greet_user()
# user_1.increment_login_attempts(1)
# user_1.number_users_system()
#
# user_1.increment_login_attempts(1)
# user_1.number_users_system()
#
# user_1.increment_login_attempts(1)
# user_1.number_users_system()
#
# user_1.reset_login_attempts(0)
# user_1.number_users_system()


# 9.6.
# class Restaurant():
#     """Класс ресторана."""
#
#     def __init__(self, restaurant_name, cuisine_type ):
#         """Инициализирует атрибуты restaurant_name и cuisine_type."""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name.title()},- {self.cuisine_type}.")
#
#     def open_restaurant(self):
#         print(f"ресторан {self.restaurant_name.title()},- открыт.\n"
#               f"Количество обслуженных посетителей - {self.number_served}")
#
#     def restaurant(self, number):
#         self.number_served = number
#         print(f" Number is now - {self.number_served}")
#
#     def set_number_served(salf, quantity):
#         salf.number_served += quantity
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super.__init__(restaurant_name, cuisine_type)
#
#     def flavors(self, list_of_varieties):
#         self. list_of_varieties = list_of_varieties
#
# varieties = IceCreamStand("от палыча", "русская кухня")
# # print(varieties.describe_restaurant())
# description.describe_restaurant()
# # varieties = IceCreamStand(['шоколадное', 'ванильное', 'клубничное'])
# description = Restaurant("москва", "русская кухня")
# description.describe_restaurant()
# description.restaurant(5)
# description.open_restaurant()


# # 9.13.
# import random as r
# class Die():
#     """класс кубика"""
#     def __init__(self, sides = 6):
#         self.sides = sides
#
#     def roll_die(self):
#         print(r.randint(1, self.sides))
#
# cube6 = Die(6)
# cube6.roll_die()
#
# cube10 = Die(10)
# cube10.roll_die()
#
# cube20 = Die(20)
# cube20.roll_die()


# # 9.14.
import random

lottery = [1,2,3,4,5,6,7,8,9,10,'a','s','d','f','g']
random_selection = random.sample(lottery, 4)
print(f"Билет содержащий эту комбинацю - {random_selection} выигал 1_000_000 долларов.")
i = 0
while True:

    while_random_selection = random.sample(lottery, 4)
    print(while_random_selection)
    i += 1

    if while_random_selection == random_selection:
        break
print(f"{while_random_selection} = {random_selection} ")
print(f"Программа просчитала - {i} вариантов")


