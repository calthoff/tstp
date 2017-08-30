

import re

line = "I love $"

matches = re.findall("\\$", line, re.IGNORECASE)

print(matches)
