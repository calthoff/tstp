

class Rectangle():
    def __init__(self, width, length):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.width * self.length

    def change_size(self, width, length):
        self.width = width
        self.length = length

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
rectangle.change_size(20, 40)
print(rectangle.calculate_area())
