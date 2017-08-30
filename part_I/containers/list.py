
color_list = ["purple", "orange", "green", "yellow", "red"]

guess = input("Guess a color in the color list:")

if guess in color_list:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")

