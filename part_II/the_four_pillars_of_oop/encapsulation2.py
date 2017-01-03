# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

class Data:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.numbers[index] = n

data_one = Data()
data_one.numbers[0] = 100
print(data_one.numbers)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.numbers)
