# for valeu in range(6):
#     print(valeu)

# numbers = list(range(2,11,2))
# print(numbers)

squares = []
for valeu in range(1,11):
    square = valeu**2
    squares.append(square)
print(squares)

squares = []
for valeu in range(1,11):
    squares.append(valeu**2)
print(squares)

squares = [valeu**2 for valeu in range(1,11)]
print(squares)