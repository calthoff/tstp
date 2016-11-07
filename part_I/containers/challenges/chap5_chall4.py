me = {
    "height": "6",
    "fav_color": "red",
    "fav_author": "Orwell"
}

answer = input("Type height, fav_color or fav_author")
if answer in me:
    result = me[answer]
    print(result)
