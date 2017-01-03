# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

def sequential_search(number_list, number):
    found = False
    for i in number_list:
        if i == number:
            found = True
            break
    return found

print(sequential_search(range(0, 100), 2))
print(sequential_search(range(0, 100), 202))
