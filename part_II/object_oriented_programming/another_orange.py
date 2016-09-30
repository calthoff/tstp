class Orange:
    print("Orange created!")

    def __init__(self):
        self.color = "orange"
        self.weight = 10

    def print_orange(self):
        print(self)
        print(self.color)
        print(self.weight)

orange = Orange()
orange.print_orange()
