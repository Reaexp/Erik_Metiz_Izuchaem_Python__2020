import random as r

print(r.randint(1,6))

players = ['alex', 'tim', 'dimon', 'angel']
first_up = r.choice(players)
print(first_up.title())