# # 9.1
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type): # тип кухни
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self): # Описание ресторана
#         print(f"Наш ресторан называется \"{self.restaurant_name.title()}\" и мы рады"
#               f" предложить Вам \n\"{self.cuisine_type}\" кухню.")
#
#     def open_restaurant(self):
#         print(f"Peсторан \"{self.restaurant_name.title()}\" - открыт.")
#
# restore = Restaurant("прага", "кавказская")
# restore.describe_restaurant()
# restore.open_restaurant()
#
# restore_2 = Restaurant("огни баку", "грузинская")
# restore_2.describe_restaurant()
# restore_2.open_restaurant()


# 9.3
class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name.title()}, {self.last_name.title()}, {self.age} лет.")

    def greet_user(self):
        print(f"Здравствуйте, {self.first_name.title()}.")

user = User("алексей", "иванов", 26)
user.describe_user()
user.greet_user()

