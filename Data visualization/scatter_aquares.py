import matplotlib.pyplot as plt

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
#
# # Назначение заголовка диаграммы и меток осей.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # Назначение размера шрифта делений на осях.
# ax.tick_params(axis='both', labelsize=14)
# plt.show()


# x_valeus = [1, 2, 3, 4, 5]
# y_valeus = [1, 4, 9, 16, 25]
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_valeus, y_valeus, s=50)
#
# # Назначение заголовка диаграммы и меток осей.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # Назначение размера шрифта делений на осях.
# ax.tick_params(axis='both', labelsize=14)
# plt.show()


# x_valeus = list(range(1, 1001))
# y_valeus = [x**2 for x in x_valeus]
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# # ax.scatter(x_valeus, y_valeus, c='red', s=5)
# ax.scatter(x_valeus, y_valeus, c=(0, 0.8, 0), s=5) # RGB
#
# # Назначение заголовка диаграммы и меток осей.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # # Назначение размера шрифта делений на осях.
# # ax.tick_params(axis='both', labelsize=14)
#
# # Назначение диапазона для каждой оси
# ax.axis([0, 1100, 0, 1100000])
# plt.show()


x_valeus = list(range(1, 1001))
y_valeus = [x**2 for x in x_valeus]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_valeus, y_valeus, c='red', s=5)
ax.scatter(x_valeus, y_valeus, c=y_valeus, cmap=plt.cm.Blues, s=5)  # RGB

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# # Назначение размера шрифта делений на осях.
# ax.tick_params(axis='both', labelsize=14)

# Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 1100000])
plt.show()
