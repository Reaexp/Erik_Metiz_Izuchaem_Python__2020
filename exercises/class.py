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
class User():
    """Класс ресторана."""

    def __init__(self, first_name, last_name, gender, age):
        """Инициализирует атрибуты restaurant_name и cuisine_type."""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(f"{self.first_name.title()}, {self.last_name.title()}; {self.gender}, {self.age}.")

    def greet_user(self):
        print(f"Рады приветствовать вас {self.first_name.title()} на нашем сайте.")


user_1 = User("alex", "reaexp", "male", 24)
user_1.describe_user()
user_1.greet_user()