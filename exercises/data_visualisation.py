import matplotlib.pyplot as plt

x_valeus = list(range(1, 5001))
y_valeus = [x**3 for x in x_valeus]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_valeus, y_valeus, c='red', s=5)
# ax.scatter(x_valeus, y_valeus, c=y_valeus, cmap=plt.cm.Blues, s=5)  # RGB

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Qube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Qube of Value", fontsize=14)

# # Назначение размера шрифта делений на осях.
# ax.tick_params(axis='both', labelsize=14)

# Назначение диапазона для каждой оси
ax.axis([0, 100, 0, 1000000])
plt.show()