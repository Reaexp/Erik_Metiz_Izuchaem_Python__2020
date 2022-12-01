class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садиться по команде."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(f"{self.name.title()} rolled over.")


my_dog = Dog('willie', 6)
print(my_dog.name.title())
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()

my_dog_2 = Dog('doger', 2)
print(my_dog_2.name.title())
print(my_dog_2.age)
my_dog_2.sit()
my_dog_2.roll_over()
