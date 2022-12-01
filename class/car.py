# class Car():
#     """A simple car model."""
#     def __init__(self, manufacturer, model, year):
#         """Initializes the attributes of the vehicle description."""
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#
#     def get_descriptive_name(self):
#         """Returns a neatly formatted description."""
#         long_name = f"{self.year} {self.manufacturer} {self.model}"
#         return long_name.title()
#
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
#
# my_new_car_2 = Car('bmw', 'turbond', 2022)
# print(my_new_car_2.get_descriptive_name())


# class Car():
#     """A simple car model."""
#     def __init__(self, manufacturer, model, year):
#         """Initializes the attributes of the vehicle description."""
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
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
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
#
# my_new_car_2 = Car('bmw', 'turbond', 2022)
# print(my_new_car_2.get_descriptive_name())
# my_new_car_2.odometer_reading = 45_000
# my_new_car_2.read_odometer()


class Car():
    """A simple car model."""
    def __init__(self, manufacturer, model, year):
        """Initializes the attributes of the vehicle description."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a neatly formatted description."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях."""
        print(f'This car has {self.odometer_reading} miles on it.')

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car_2 = Car('bmw', 'turbond', 2022)
print(my_new_car_2.get_descriptive_name())
my_new_car_2.odometer_reading = 45_000
my_new_car_2.read_odometer()
