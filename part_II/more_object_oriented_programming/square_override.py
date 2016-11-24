class Shape():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


class Square(Shape):
    def calculate_area(self):
        return self.width * self.length

    def print_size(self):
        print("I am a square that is {} by {}".format(self.width, self.length))

a_square = Square(20, 20)
a_square.print_size()
