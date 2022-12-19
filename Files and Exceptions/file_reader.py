# with open('pi_digits.txt') as file_object:  # Конструкция с ключевым словом with закрывает файл после того,
#     # как надобность в нем отпадет.
#     contents = file_object.read()
# # print(contents)
# print(contents.rstrip())

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         # print(line)  # Пустые строки появляются из-за того, что каждая строка в текстовом файле
#         # завершается невидимым символом новой строки.
#         print(line.rstrip()) #  Вызов rstrip() в команде print удаляет лишние пустые строки

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip()) #  Вызов rstrip() в команде print удаляет лишние пустые строки