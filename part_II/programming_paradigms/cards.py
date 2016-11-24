cards = []
suits = ["spades", "hearts", "diamonds", "clubs"]
players = []


def create_cards():
    for i in range(2, 52):
        for suit in suits:
            cards.append((i, suit))


def create_players():
    for i in range(2):
        players.append([])

    middle = int(len(cards) / 2)
    players[0].append(cards[0:middle])
    players[1].append(cards[middle:])


def play_game():
    for card in players[0]:
        print(card)

    for card in players[1]:
        print(card)


create_cards()
create_players()
play_game()
