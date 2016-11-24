my_list = list()

with open("my_file.txt", "r") as my_file:
        my_list.append(my_file.read())


print(my_list)
