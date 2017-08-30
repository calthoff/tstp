

def sequential_search(number_list, number):
    found = False
    for i in number_list:
        if i == number:
            found = True
            break
    return found

print(sequential_search(range(0, 100), 2))
print(sequential_search(range(0, 100), 202))
