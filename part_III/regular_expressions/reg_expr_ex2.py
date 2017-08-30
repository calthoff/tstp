
import re

line = """The numbers 172 can be found on the back of the U.S. $5 dollar bill in the bushes at the base
       of the Lincoln Memorial."""

matchObj = re.findall('\d+', line)

if matchObj:
    print(matchObj)
else:
    print("No match!")
