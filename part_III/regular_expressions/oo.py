
import re


sentence = "Two is a number and too is not."


match = re.findall("t[ow]o", sentence, re.IGNORECASE)
print(match)
