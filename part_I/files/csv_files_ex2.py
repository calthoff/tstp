
import csv

# make sure you’ve created the file from the previous example

with open("self_taught.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        print(",".join(row))
