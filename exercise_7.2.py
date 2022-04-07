table = input('How many seats do you want to book a table in a restaurant?')
table = int(table)

if table > 8:
    print("You'll have to wait a bit.")
else:
    print("Your table is ready.")