

songs = {"Like a Rolling Stone": "Bob Dylan",
         "A Day in the Life": "The Beatles",
         "Here Comes the Sun": "The Beatles",
         "Johnny B. Goode": "Chuck Berry",
         "Stand By Me": "John Lennon",
         "James Brown": "I got You (I Feel Good)"
         }

song_name = input("Type a song name in the dictionary:")
if song_name in songs:
    artist = songs[song_name]
    print(artist)
else:
    print("The song name you requested is not available.")
