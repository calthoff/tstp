# IF YOU ARE READING THIS YOU ARE READING
# AN OUTDATED VERSION OF THE BOOK. THE NEW VERSION
# IS MUCH BETTER.
# I am working with Amazon to resolve this.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

the_shows = ["Game of Thrones", "Narcos", "Vice"]
i = 0
for show in the_shows:
    new_show = the_shows[i]
    new_show = new_show.upper()
    the_shows[i] = new_show
    i += 1

print(the_shows)

