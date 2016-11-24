class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def print_size(self):
        print("{} by {}".format(self.width, self.length))

my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()
