
import csv

with open("self_taught.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    spamwriter.writerow(["one", "two", "three"])
    spamwriter.writerow(["four", "five", "six"])
