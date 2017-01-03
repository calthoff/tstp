# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

class Orange:
    print("Orange created!")

    def __init__(self):
        self.color = "orange"
        self.weight = 10

    def print_orange(self):
        print(self.color)
        print(self.weight)
        self.color = "dark orange"
        self.weight = 20
        print(self.color)
        print(self.weight)

orange = Orange()
orange.print_orange()
