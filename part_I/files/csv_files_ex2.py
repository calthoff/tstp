import csv

# make sure you’ve created the file from the previous example

with open("my_file.csv", "r") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        print(",".join(row))
