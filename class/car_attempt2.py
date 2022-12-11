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