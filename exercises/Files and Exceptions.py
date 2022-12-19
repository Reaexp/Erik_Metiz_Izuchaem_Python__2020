#10.1

with open('K:\My_disk_Alex\Programing\Python\project\Erik_Metiz_Izuchaem_Python__2020\learning_python.txt') as file_python:
    # reader = file_python.read()
    # print(reader)

#     reader = file_python.readline()
# for line in reader:
#     print(line)

#     reader = file_python.readlines()
# for line in reader:
#     print(line.rstrip())


    reader = file_python.readlines()
for line in reader:
    line = line.replace("Python", "C")
    print(line.rstrip())

