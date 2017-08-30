

class Orange:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        print("Orange object created!")

an_orange = Orange(10, "dark orange")

an_orange.weight = 100
an_orange.color = "light orange"

print(an_orange.weight)
print(an_orange.color)
