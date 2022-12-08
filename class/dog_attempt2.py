class Dog():
    """Простая модель собаки."""
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(f"{self.name} сидит.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(f"{self.name} перекатывается.")


my_dog = Dog("Пёс", "6")
print(f"Мою собаку зовут \"{my_dog.name}\", ей {my_dog.age} лет.")
my_dog.sit()

my_dog_2 = Dog("Тузик", "3")
print(f"Мою собаку зовут \"{my_dog_2.name}\", ей {my_dog_2.age} лет.")
my_dog_2.roll_over()
