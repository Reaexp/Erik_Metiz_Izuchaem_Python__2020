filename = 'programming.txt'

with open(filename, 'w') as fileobject:
    fileobject.write("I love you!\n")
    fileobject.write("And, i love you!!!\n\n")


with open(filename, 'a') as fileobject:
    fileobject.write("I also love finding meaning in large datasets.\n")
    fileobject.write("I love creating apps that can run in a browser.")