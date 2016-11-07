import csv

with open("new_file.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    spamwriter.writerow(["one", "two", "three"])
    spamwriter.writerow(["four", "five", "six"])
