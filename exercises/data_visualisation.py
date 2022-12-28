# import matplotlib.pyplot as plt
#
# x_valeus = list(range(1, 5001))
# y_valeus = [x**3 for x in x_valeus]
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_valeus, y_valeus, c='red', s=5)
# # ax.scatter(x_valeus, y_valeus, c=y_valeus, cmap=plt.cm.Blues, s=5)  # RGB
#
# # Назначение заголовка диаграммы и меток осей.
# ax.set_title("Qube Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Qube of Value", fontsize=14)
#
# # # Назначение размера шрифта делений на осях.
# # ax.tick_params(axis='both', labelsize=14)
#
# # Назначение диапазона для каждой оси
# ax.axis([0, 100, 0, 1000000])
# plt.show()


#15.3
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, "K:\My_disk_Alex\Programing\Python\project\Erik_Metiz_Izuchaem_Python__2020\Data visualization")
from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной
while True:
    # Построение случайног облуждания.
    rw = RandomWalk(5_000)
    rw.full_walk()

    # Нанесение точек на диаграмму.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_valeus, rw.y_valeus, c=rw.y_valeus, cmap=plt.cm.Blues, edgecolors='none', linewidth=1)
    ax.plot(rw.x_valeus, rw.y_valeus, linewidth=1)

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