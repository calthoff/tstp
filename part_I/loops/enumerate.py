# IF YOU ARE READING THIS YOU ARE READING
# AN OUTDATED VERSION OF THE BOOK. THE NEW VERSION
# IS MUCH BETTER.
# I am working with Amazon to resolve this.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

intense_shows = ["Game of Thrones", "Narcos", "Vice"]
for i, show in enumerate(intense_shows):
    new_show = intense_shows[i]
    new_show = new_show.upper()
    intense_shows[i] = new_show
    i += 1

print(intense_shows)
