import csv

with open("my_file.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        print(",".join(row))
