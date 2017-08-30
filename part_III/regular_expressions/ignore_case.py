

import re

line = "Beautiful is better than ugly."

matches = re.findall("beautiful", line, re.IGNORECASE)

print(matches)
