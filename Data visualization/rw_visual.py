import matplotlib.pyplot as plt

from random_walk import RandomWalk

# # Построение случайног облуждания.
# rw = RandomWalk()
# rw.full_walk()
#
# # Нанесение точек на диаграмму.
# plt.style.use('classic')
# fig, ax = plt.subplots()
# ax.scatter(rw.x_valeus, rw.y_valeus, s=15)
# plt.show()

# # Новые блуждания строятся до тех пор, пока программа остается активной
# while True:
#     # Построение случайног облуждания.
#     rw = RandomWalk()
#     rw.full_walk()
#
#     # Нанесение точек на диаграмму.
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     ax.scatter(rw.x_valeus, rw.y_valeus, s=15)
#     plt.show()
#
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == "n":
#         break


# # Новые блуждания строятся до тех пор, пока программа остается активной
# while True:
#     # Построение случайног облуждания.
#     rw = RandomWalk()
#     rw.full_walk()
#
#     # Нанесение точек на диаграмму.
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_valeus, rw.y_valeus, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#     plt.show()
#
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == "n":
#         break


# #Начальные и конечные точки

# # Новые блуждания строятся до тех пор, пока программа остается активной
# while True:
#     # Построение случайног облуждания.
#     rw = RandomWalk()
#     rw.full_walk()
#
#     # Нанесение точек на диаграмму.
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_valeus, rw.y_valeus, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#
#     # Выделение первой и последней точек.
#     ax.scatter(0, 0, c='green', edgecolors='none', s=100)
#     ax.scatter(rw.x_valeus[-1], rw.y_valeus[-1], c='red', edgecolors='none', s=100)
#     plt.show()
#
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == "n":
#         break


# Удаление осей

# # Новые блуждания строятся до тех пор, пока программа остается активной
# while True:
#     # Построение случайног облуждания.
#     rw = RandomWalk()
#     rw.full_walk()
#
#     # Нанесение точек на диаграмму.
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_valeus, rw.y_valeus, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
#
#     # Выделение первой и последней точек.
#     ax.scatter(0, 0, c='green', edgecolors='none', s=100)
#     ax.scatter(rw.x_valeus[-1], rw.y_valeus[-1], c='red', edgecolors='none', s=100)
#     # Удаление осей
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#     plt.show()
#
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == "n":
#         break


# # Добавление точек
#
# # Новые блуждания строятся до тех пор, пока программа остается активной
# while True:
#     # Построение случайног облуждания.
#     rw = RandomWalk(1_000_000)
#     rw.full_walk()
#
#     # Нанесение точек на диаграмму.
#     plt.style.use('classic')
#     fig, ax = plt.subplots()
#     point_numbers = range(rw.num_points)
#     ax.scatter(rw.x_valeus, rw.y_valeus, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
#
#     # Выделение первой и последней точек.
#     ax.scatter(0, 0, c='green', edgecolors='none', s=100)
#     ax.scatter(rw.x_valeus[-1], rw.y_valeus[-1], c='red', edgecolors='none', s=100)
#     # Удаление осей
#     ax.get_xaxis().set_visible(False)
#     ax.get_yaxis().set_visible(False)
#     plt.show()
#
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == "n":
#         break


# Изменение размера диаграммы для заполнения экрана

# Новые блуждания строятся до тех пор, пока программа остается активной
while True:
    # Построение случайног облуждания.
    rw = RandomWalk(50_000)
    rw.full_walk()

    # Нанесение точек на диаграмму.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_valeus, rw.y_valeus, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Выделение первой и последней точек.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_valeus[-1], rw.y_valeus[-1], c='red', edgecolors='none', s=100)
    # Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break