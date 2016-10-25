intense_shows = ["Game of Thrones", "Narcos", "Vice"]
i = 0
for show in intense_shows:
    new_show = intense_shows[i]
    new_show = new_show.upper()
    intense_shows[i] = new_show
    i += 1

print(intense_shows)
