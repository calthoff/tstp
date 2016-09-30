class Adult():
    def __init__(self, name, height, weight, eye_color):
        # height is in feet, weight in lbs.
        self.name = name
        self.height = height
        self.weight = weight
        self.eye_color = eye_color

    def print_name(self):
        print(self.name)


class Kid(Adult):
    def print_cartoon(self, favorite_cartoon):
        print("{}'s favorite cartoon is {}".format(self.name, favorite_cartoon))


child = Kid("Lauren", 3, 50, "blue")
print(child.name)
print(child.height)
print(child.weight)
print(child.eye_color)
child.print_name()
child.print_cartoon('DuckTales')
