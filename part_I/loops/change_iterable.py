

the_shows = ["Game of Thrones", "Narcos", "Vice"]
i = 0
for show in the_shows:
    new_show = the_shows[i]
    new_show = new_show.upper()
    the_shows[i] = new_show
    i += 1

print(the_shows)

