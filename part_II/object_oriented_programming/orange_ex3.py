class Orange:
    def __init__(self, weight, color, mold):
        """all weights are in oz"""
        self.weight = weight
        self.color = color
        self.mold = mold

    def rot(self, days, temperature):
        self.mold = days * (temperature * .1)


orange = Orange(10, 'orange', 2)
print(orange.weight)
print(orange.color)
print(orange.mold)

orange.weight = 100
print(orange.weight)

orange.rot(50, 100)
print(orange.mold)
