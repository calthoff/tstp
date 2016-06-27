class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
bob2 = bob
print(bob is bob2)

another_bob = Person()
print(bob is another_bob)
