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
# class User():
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def describe_user(self):
#         print(f"{self.first_name.title()}, {self.last_name.title()}, {self.age} лет.")
#
#     def greet_user(self):
#         print(f"Здравствуйте, {self.first_name.title()}.")
#
# user = User("алексей", "иванов", 26)
# user.describe_user()
# user.greet_user()


# 9.4
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type): # тип кухни
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 2 # количество обслуживаемых
#
#     def describe_restaurant(self): # Описание ресторана
#         print(f"Наш ресторан называется \"{self.restaurant_name.title()}\" и мы рады"
#               f" предложить Вам \n\"{self.cuisine_type}\" кухню.")
#
#     def open_restaurant(self):
#         print(f"Peсторан \"{self.restaurant_name.title()}\" - открыт.")
#
#     def set_number_served(self, number):
#         self.number_served = number
#
#     def increment_number_served(self, increment):
#         self.number_served += increment


# restore = Restaurant("прага", "кавказская")
# restore.describe_restaurant()
# restore.open_restaurant()
#
# restore_2 = Restaurant("огни баку", "грузинская")
# restore_2.describe_restaurant()
# restore_2.open_restaurant()

# restaurant = Restaurant('огни баку', 'азербайджанская')
# restaurant.describe_restaurant()
# print(restaurant.number_served)

# restaurant = Restaurant('огни баку', 'азербайджанская')
# restaurant.describe_restaurant()
# restaurant.set_number_served(7)
# print(restaurant.number_served)
#
# restaurant.increment_number_served(2)
# print(restaurant.number_served)
#
# restaurant.increment_number_served(1)
# print(restaurant.number_served)


# # 9.5
# class User():
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 0 # попытки входа в систему
#
#     def describe_user(self):
#         print(f"{self.first_name.title()}, {self.last_name.title()}, {self.age} лет.")
#
#     def greet_user(self):
#         print(f"Здравствуйте, {self.first_name.title()}.")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
# user = User("алексей", "иванов", 26)
# user.describe_user()
# user.greet_user()
# print(user.login_attempts)
#
# user.increment_login_attempts()
# print(user.login_attempts)
#
# user.increment_login_attempts()
# print(user.login_attempts)
#
# user.reset_login_attempts()
# print(user.login_attempts)


# # 9.6
# class Restaurant():
#     def __init__(self, restaurant_name, cuisine_type): # тип кухни
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 2 # количество обслуживаемых
#
#     def describe_restaurant(self): # Описание ресторана
#         print(f"Наш ресторан называется \"{self.restaurant_name.title()}\" и мы рады"
#               f" предложить Вам \n\"{self.cuisine_type}\" кухню.")
#
#     def open_restaurant(self):
#         print(f"Peсторан \"{self.restaurant_name.title()}\" - открыт.")
#
#     def set_number_served(self, number):
#         self.number_served = number
#
#     def increment_number_served(self, increment):
#         self.number_served += increment
#
# class IceCreamStand(Restaurant):
#     def __init__(self, restaurant_name, cuisine_type):
#         super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
#         self.flavors = ["сливочное", "шоколадное", "ванильное"]
#
#     def list_output(self):
#         print(f"Мы рады предложить Вам {self.flavors[0]}, {self.flavors[1]} и {self.flavors[2]} мороженное. ")
#
#
# restore = Restaurant("прага", "кавказская")
# restore.describe_restaurant()
# restore.open_restaurant()
#
# restore_2 = Restaurant("огни баку", "грузинская")
# restore_2.describe_restaurant()
# restore_2.open_restaurant()
#
# restaurant = Restaurant('огни баку', 'азербайджанская')
# restaurant.describe_restaurant()
# print(restaurant.number_served)
#
# restaurant = IceCreamStand('холодок', 'освежающая')
# restaurant.describe_restaurant()
# restaurant.list_output()


# 9.7
# 9.8
# class User():
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 0 # попытки входа в систему
#
#     def describe_user(self):
#         print(f"{self.first_name.title()}, {self.last_name.title()}, {self.age} лет.")
#
#     def greet_user(self):
#         print(f"Здравствуйте, {self.first_name.title()}.")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
# class Admin(User):
#     def __init__(self, first_name, last_name, age):
#         super(Admin, self).__init__(first_name, last_name, age)
#         self.priv = Privileges()
#
#
# class Privileges():
#     def __init__(self):
#         self.privileges = ["добавлять сообщения", "удалять пользователей", "банить пользователей"]
#
#     def show_privileges(self):
#         print(f"Вы имеете право: {self.privileges[0]}, {self.privileges[1]}, {self.privileges[2]}. ")
#
#
# user = User("алексей", "иванов", 26)
# user.describe_user()
# user.greet_user()
# print(user.login_attempts)
#
# user.increment_login_attempts()
# print(user.login_attempts)
#
# user.increment_login_attempts()
# print(user.login_attempts)
#
# user.reset_login_attempts()
# print(user.login_attempts)
#
# admin = Admin("Иван", "петров", 45)
# admin.describe_user()
# admin.greet_user()
# admin.priv.show_privileges()

#9.9
class Car():
    """простая модель автомобиля."""
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 25

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное имя."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f"Данный автомобиль имеет пробег - {self.odometer_reading} км.")

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре."""
        # Устанавливает на одометре заданное значение.
        # При попытке обратной подкрутки изменение отклоняется.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете отмотать пробег...стыдно должно быть...")

    def increment_odometer(self, miles):
        """Увеличивает показание одометра с заданным приращением."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"У автомобиля '{self.manufacturer.title()} {self.model.title()}' есть бензобак.")

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    # Инициализирует атрибуты класса-родителя.
    # Затем инициализирует атрибуты, специфические для электромобиля.

    def __init__(self, manufacturer, model, year):
        """Инициализирует атрибуты класса родителя."""
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"У данного автомобиля нет бензобака.")

class Battery():
    """Модель аккумулятора авто."""
    def __init__(self, battery_size = 75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит инф. о мощности аккумулятора."""
        print(f"Заряд аккумулятора равен - {self.battery_size} kWh")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"Эта машина может проехать около {range} на полной зарядке.")

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(28)
my_new_car.read_odometer()
my_new_car.increment_odometer(10)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

my_tesla = ElectricCar('tesla', 'model s', '2020')
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(128)
my_tesla.read_odometer()
my_tesla.increment_odometer(100)
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()









