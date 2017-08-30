
places = dict()

new_york_coordinates = (40.7128, 74.0059)
new_york_celebrities = ["Sean Parker", "Rosie O'Donnel", "Neil Patrick Harris"]
new_york_facts = {"state": "NY", "country": "America"}

new_york_data = dict()
new_york_data["new_york_coordinates"] = new_york_coordinates
new_york_data["new_york_celebrities"] = new_york_celebrities
new_york_facts["new_york_facts"] = new_york_facts

places["New York"] = new_york_data

ny_info = places["New York"]
print(ny_info["new_york_coordinates"])
print(new_york_data["new_york_celebrities"])
print(new_york_facts["new_york_facts"])
