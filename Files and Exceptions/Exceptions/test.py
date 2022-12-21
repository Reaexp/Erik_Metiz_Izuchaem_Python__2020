import json

user_name = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(user_name.title(), f)
    print(f"We'll remember you when you come back, {user_name.title()}")