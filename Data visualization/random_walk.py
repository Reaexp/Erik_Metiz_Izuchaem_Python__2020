from random import choice

class RandomWalk():
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=5000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points

        # Все блуждания начинаются с точки (0, 0)
        self.x_valeus = [0]
        self.y_valeus = [0]

    def full_walk(self):
        """Вычисляет все точки блуждания."""
        # Шаги генерируются до достижения нужной длинны.
        while len(self.x_valeus) < self.num_points:

            # Определение направления и длинны перемещения
            x_direction = choice([1, -1])
            x_distanse = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distanse

            y_direction = choice([1, -1])
            y_distanse = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distanse

            # Отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений
            x = self.x_valeus[-1] + x_step
            y = self.y_valeus[-1] + y_step

            self.x_valeus.append(x)
            self.y_valeus.append(y)