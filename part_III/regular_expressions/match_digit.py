
import re

line = "123 do you copy? 345 hello?"

matches = re.findall("\d", line, re.IGNORECASE)

print(matches)
