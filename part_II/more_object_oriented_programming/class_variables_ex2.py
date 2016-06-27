class Person:
    people_list = []

    def __init__(self, name):
        self.name = name
        self.people_list.append(name)

bob = Person('Ada Lovelace')
joe = Person('Grace Hopper')
jane = Person('Leah Culver')
print(Person.people_list)
