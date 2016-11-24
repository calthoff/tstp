import copy

my_list = [1, 2, 3]
list_copy = copy.deepcopy(my_list)

my_list.append(4)

print(my_list)
print(list_copy)
