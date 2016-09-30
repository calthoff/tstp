class Adult():
    def __init__(self, name, height, weight, eye_color):
        """height is in feet, weight in lbs."""
        self.name = name
        self.height = height
        self.weight = weight
        self.eye_color = eye_color

    def print_name(self):
        print(self.name)

tom = Adult("Tom", 6, 150, "brown")
print(tom.name)
print(tom.height)
print(tom.weight)
print(tom.eye_color)
tom.print_name()