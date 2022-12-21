# filename = 'alice.txt'
#
# with open(filename, encoding='utf-8') as f:
#     contents = f.read()

# filename = 'alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file '{filename}' does not exist.")

# filename = 'alice.txt'
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file '{filename}' does not exist.")
#
# else:
#     # Подсчитаем приблизительное количество строк в файле
#     words = contents.split()
#     num_words = len(words)
#     print(f"The file '{filename}' has about {num_words} words.")

# def count_words(filename):
#     """ Подсчитаем приблизительное количество строк в файле"""
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         # print(f"Sorry, the file '{filename}' does not exist.")
#         pass
#
#     else:
#
#         words = contents.split()
#         num_words = len(words)
#         print(f"The file '{filename}' has about {num_words} words.")
#
# # filename = 'alice.txt'
# # count_words(filename)
#
# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt' ]
# for filename in filenames:
#     count_words(filename)

lines = 'alice.txt'
with open(lines, encoding='utf-8') as l:
    contents = l.readlines()

for line in contents:
    a = line.count('li')
    b = line.lower().count('li')
    print(a)
    print(b)


