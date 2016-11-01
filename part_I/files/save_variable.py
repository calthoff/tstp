my_list = list()

with open("my_file.txt", "r") as my_file:
    for line in my_file.read():
        my_list.append(line)


print(my_list)
