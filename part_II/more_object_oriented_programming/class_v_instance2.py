class Rectangle():
    rectangles_created = []

    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.rectangles_created.append((self.width, self.length))

    def print_size(self):
        print("{} by {}".format(self.width, self.length))

my_rectangle1 = Rectangle(10, 24)
my_rectangle2 = Rectangle(20, 40)
my_rectangle3 = Rectangle(100, 200)

print(Rectangle.rectangles_created)
