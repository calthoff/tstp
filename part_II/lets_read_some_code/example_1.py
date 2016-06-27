class Tree:
    def __init__(self, species, height, width):
        self.species = species
        self.color = "yellow"
        self.height = height
        self.width = width

    def change_season(self, season):
        seasons = {'fall': 'yellow', 'winter': None, 'spring': 'green', 'summer': 'brown'}
        if season not in seasons:
            raise ValueError("not a valid season")
        self.color = seasons[season]

pine = Tree('pine', 100, 5)
maple = Tree('maple', 200, 20)

print(pine.color)
print(maple.color)

pine.change_season('summer')
maple.change_season('spring')

print(pine.color)
print(maple.color)
