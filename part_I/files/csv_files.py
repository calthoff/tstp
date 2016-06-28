import csv

with open("my_file.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    spamwriter.writerow(["one", "two", "three"])
