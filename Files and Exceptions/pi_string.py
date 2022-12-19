# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     # pi_string += line.rstrip()
#     pi_string += line.strip()
#
# print(pi_string)
# print(len(pi_string))

# filename = 'pi_million_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     # pi_string += line.rstrip()
#     pi_string += line.strip()
#
# print(f"{pi_string[:52]}...")
# # print(pi_string)
# print(len(pi_string[:52]))

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()
    pi_string += line.strip()

birthday = input("Введите дату вашего рождения в формате ддммгг: ")
if birthday in pi_string:
    print("Ваш день рожденья указан в первом миллионе числа пи!")
else:
    print("Вам не повезло!!!")