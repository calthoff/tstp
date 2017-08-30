

rock_songs = []
country_songs = []


def collect_songs():
    song_prompt= "Enter the name of your song."
    song_type = None
    while True:
        song_type = input("Type rock or country to add a new song. q to quit:")
        if song_type == "q":
            break
        if song_type == "rock":
            rock_song = input(song_prompt)
            rock_songs.append(rock_song)

        elif song_type ==("country"):
            country_song = input(song_prompt)
            country_songs.append(country_song)

        else:
            print("Invalid song type.")
    print(rock_songs)
    print(country_songs)

collect_songs()
