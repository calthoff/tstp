class Mammal:
    def __init__(self, name):
        self.hunger = 100
        self.tired = 100
        self.name = name

    def print_result(self, amount, action):
        print("{} {} decreased by {}.".format(self.name, action, amount))

    def eat(self, decrease):
        self.hunger -= decrease
        self.print_result(decrease, 'hunger')

    def sleep(self, decrease):
        self.tired -= decrease
        self.print_result(decrease, 'tiredness')


class Dolphin(Mammal):
    pass


class Tiger(Mammal):
    def sleep(self, decrease):
        self.tired -= decrease
        print("The tiger is really tired!")

dolphin = Dolphin('dolphin')
dolphin.eat(10)
dolphin.sleep(10)

tiger = Tiger('tiger')
tiger.eat(10)
tiger.sleep(10)


class Tiger(Mammal):
    def sleep(self, decrease):
        super().sleep(decrease)
        print("The tiger is really tired!")


tiger = Tiger('tiger')
tiger.eat(10)
tiger.sleep(10)
