# print(5/0)

# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

print("Give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.")
while True:
    meaning = []
    while True:
        try:
            first_number = input("\nFirst number: ")
            if first_number == 'q':
                meaning.append(first_number)
                break
            first_number = int(first_number)
            break
        except ValueError:
            print("Enter a number!")
    if meaning == ['q']:
        break

    while True:
        try:
            second_number = input("\nSecond number: ")
            if second_number == 'q':
                meaning.append(second_number)
                break
            second_number = int(second_number)
            break
        except ValueError:
            print("Enter a number!")
    if meaning == ['q']:
        break

    try:
        answer = int(first_number) / (second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("вы не ввели число...")
        break
    else:
        print(answer)
        break
