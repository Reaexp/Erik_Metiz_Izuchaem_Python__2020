# 8.1
# def display_message ():
#     print("В этой главе мы изучаем функции. УРА!!!")
# display_message()

# 8.2
# def favorite_book(name):
#     print(f"My favorite book is {name} ")
#
# favorite_book("Эрик Мэтиз_Изучаем Python.")

# 8.3
# def make_shirt(size, text):
#     print(f"Вы заказали футболку {size} размера с надписью - '{text.title()}'.")
# make_shirt("52","hello world")

# 8.4
# def make_shirt(size="L", text="I love Python"):
#     print(f"Вы заказали футболку {size} размера с надписью - '{text.title()}'.")
# make_shirt()
# make_shirt("52","hello world")

# 8.5
def discribe_city(city, country="Россия"):
    print(f" {country.title()} великая страна. В ней есть город '{city.title()}'.")
discribe_city("Москва")
discribe_city("Владивосток")