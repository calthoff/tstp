class Shape():
    def print(self):
        print("I am a shape.")


class Square(Shape):
    def print(self):
        super().print()
        print("Specifically, I am a square.")

square = Square()
square.print()
