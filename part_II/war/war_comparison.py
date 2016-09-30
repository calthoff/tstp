class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = [None, None,"2", "3", "4", "5", "6", "7", "8", "9",
              "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, value, suit):
        """suit and value should be integers"""
        self.value = value
        self.suit = suit

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]


card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 < card2)
