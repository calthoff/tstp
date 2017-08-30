

class Orange():
    def __init__(self):
        """all weights are in oz"""
        self.weight = 6
        self.color = 'orange'
        self.mold = 0

    def rot(self, days, temperature):
        self.mold = days * (temperature * .1)


orange = Orange()
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)
