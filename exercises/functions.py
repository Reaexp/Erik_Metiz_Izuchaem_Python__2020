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
# def discribe_city(city, country="Россия"):
#     print(f" {country.title()} великая страна. В ней есть город '{city.title()}'.")
# discribe_city("Москва")
# discribe_city("Владивосток")

# 8.6
# def city_country(city, country):
#     general_name = (f"{city}, {country}").title()
#     return general_name
#
# purpose = city_country("россия", "москва")
# print(purpose)


# def city_country(city, country):
#     general_name = f"\"{city}\", \"{country}\""
#     return general_name.title()
#
#
# purpose = city_country("россия", "москва")
# print(purpose)
# purpose = city_country("беларусь", "минск")
# print(purpose)
# purpose = city_country("россия", "киев")
# print(purpose)


# 8.7
# def make_album(artist_name, album_title):
#     musician = {'a_name': artist_name.title(), 'a_title': album_title.upper()}
#     return musician
#
#
# album = make_album('пугачева', 'Алые паруса')
# print(album)
# album = make_album('галкин', 'петушок')
# print(album)


# def make_album(artist_name, album_title, track = None):
#     musician = {'a_name': artist_name.title(), 'a_title': album_title.upper()}
#     if track:
#         musician['track'] = track
#     return musician
#
#
# album = make_album('пугачева', 'Алые паруса')
# print(album)
# album = make_album('галкин', 'петушок', 23)
# print(album)

# 8.8
# def make_album(artist_name, album_title):
#     album = {'a_name': artist_name.title(), 'a_title': album_title.upper()}
#     return album
#
# while True:
#     print('Введите имя артиста и название альбома. ')
#     print('Для остановки программы напишите "Обама Чмо"')
#
#     name = input("имя: ")
#     if "Обама Чмо" == name:
#         break
#     album = input("альбом: ")
#     if "Обама Чмо" == album:
#         break
#     full_album = make_album(name, album)
#     print(full_album)
#     break

# 8.9
# message_list = ["Hello!", "how do you do?", "whatsapp man?"]
#
# def show_messages(message_list):
#     while message_list:
#         print(message_list.pop(0))
#
# show_messages(message_list)

# 8.10
# send_messages = ["Hello!", "how do you do?", "whatsapp man?"]
# sent_messages = []
#
# def show_messages(send_messages):
#     while send_messages:
#         message = send_messages.pop(0)
#         print(message)
#         sent_messages.append(message)
#
# show_messages(send_messages)
#
# print(sent_messages)

# 8.11
send_messages = ["Hello!", "how do you do?", "whatsapp man?"]
sent_messages = []

def show_messages(send_messages):
    while send_messages:
        message = send_messages.pop(0)
        print(message)
        sent_messages.append(message)

show_messages(send_messages[:])

print(send_messages)
print(sent_messages)