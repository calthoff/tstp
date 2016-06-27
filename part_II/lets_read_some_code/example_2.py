from random import randint


class Player:
    def __init__(self, player_name):
        self.name = player_name


class Game:
    def __init__(self):
        self.score = 0

    def play(self, player):
        guess = None
        print("Welcome {}".format(player.name))
        while guess != 'q':
            number = randint(0, 10)
            guess = input("Guess a number from 0 to 10:")
            try:
                guess = int(guess)
            except ValueError:
                print('Please enter a number:')
                continue
            if guess == number:
                print('Great job {}. You win!'.format(player.name))
                self.score += 10
                print("The score is {}.".format(self.score))
            else:
                print('Sorry {}. You lose! The number was {}'.format(player.name, number))
                self.score -= 1
                print("The score is {}.".format(self.score))

game = Game()
game.play(Player("Bernie"))
