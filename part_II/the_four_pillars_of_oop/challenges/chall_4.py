class Horse():
    def __init__(self, name):
        self.name = name


class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

harry_the_horse = Horse("Harry")
the_rider = Rider("Sally", harry_the_horse)

print(the_rider.horse.name)
