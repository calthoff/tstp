

class Shape():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def print_size(self):
        print("{} by {}".format(self.width, self.length))


class Square(Shape):
    def calculate_area(self):
        return self.width * self.length

a_square = Square(20, 20)
print(a_square.calculate_area())
