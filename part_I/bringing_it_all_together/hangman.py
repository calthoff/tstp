

def hangman():
    stage = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|             "]
    word = "cat"
    score_board = ['__'] * len(word)
    print 'Welcome to Hang Man'
    win = False
    while stage < len(stages) - 1:
        print '\n'
        guess = raw_input("Guess a letter")
        if guess in word:
            score_board[word.index(guess)] = guess
        else:
            stage += 1
        print(' '.join(score_board))
        print '\n'.join(stages[0: stage + 1])
        if '__' not in score_board:
            print 'You win! The word was:'
            print(' '.join(score_board))
            win = True
            break
    if not win:
        print '\n'.join(stages[0: stage])
        print 'You lose!'

hangman()

