class Parent():
    def __init__(self):
        self.name = 'Ricky'
        self.eye_color = 'brown'

    def print_name(self):
        print(self.name)


class Child(Parent):
    @staticmethod
    def print_cartoon(favorite_cartoon):
        print(favorite_cartoon)

child = Child()
print(child.eye_color)
child.print_name()
child.print_cartoon('DuckTales')
