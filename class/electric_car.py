# class Car():
#     """A simple car model."""
#
#     def __init__(self, manufacturer, model, year):
#         """Initializes the attributes of the vehicle description."""
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 500
#
#     def get_descriptive_name(self):
#         """Returns a neatly formatted description."""
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Выводит пробег машины в милях."""
#         print(f'This car has {self.odometer_reading} miles on it.')
#
#     def update_odometer(self, mileage):
#         """Устанавливает на одометре заданное значение.
# При попытке обратной подкрутки изменение отклоняется."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometr(self, miles):
#         """"Увеличивает показания одометра с заданным приращением."""
#         self.odometer_reading += miles
#
#     def fill_gas_tank(self):
#         """У электромобилей нет бензобака."""
#         print("This car doesn't need a gas tank!")
#
#
# # class ElectricCar(Car):
# #     """Представляет аспекты авто, специфические для электрокара."""
# #
# #     def __init__(self, manufacturer, model, year):
# #         """инициализирует атрибуты класса - родителя"""
# #         super().__init__(manufacturer, model, year)
#
# class ElectricCar(Car):
#     """Представляет аспекты авто, специфические для электрокара."""
#
#     def __init__(self, manufacturer, model, year):
#         """инициализирует атрибуты класса - родителя.
#         Инициализирует атрибуты, специфические для электромобиля."""
#         super().__init__(manufacturer, model, year)
#         self.battery_size = 75
#
#     def describe_battery(self):
#         """Выводит инф. о мощности аккум."""
#         print(f"This cor has a {self.battery_size} - kWh battery.")
#
#
# my_tesla = ElectricCar('tesla', 'model-s', 2020)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()
#
# my_new_car = Car('bmw', 'turbond', 2022)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(25_000)
# my_new_car.read_odometer()
#
# my_new_car.increment_odometr(500)
# my_new_car.read_odometer()


class Car():
    """A simple car model."""

    def __init__(self, manufacturer, model, year):
        """Initializes the attributes of the vehicle description."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 500

    def get_descriptive_name(self):
        """Returns a neatly formatted description."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        """Устанавливает на одометре заданное значение.
При попытке обратной подкрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometr(self, miles):
        """"Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("This car doesn't need a gas tank!")


# class ElectricCar(Car):
#     """Представляет аспекты авто, специфические для электрокара."""
#
#     def __init__(self, manufacturer, model, year):
#         """инициализирует атрибуты класса - родителя"""
#         super().__init__(manufacturer, model, year)

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size = 75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит инф. о мощности аккум."""
        print(f"This cor has a {self.battery_size} - kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Представляет аспекты авто, специфические для электрокара."""

    def __init__(self, manufacturer, model, year):
        """инициализирует атрибуты класса - родителя.
        Инициализирует атрибуты, специфические для электромобиля."""
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model-s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()

my_new_car = Car('bmw', 'turbond', 2022)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(25_000)
my_new_car.read_odometer()

my_new_car.increment_odometr(500)
my_new_car.read_odometer()
