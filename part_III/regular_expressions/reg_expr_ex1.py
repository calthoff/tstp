import re

line = "Match this."

matchObj = re.search('this', line)

if matchObj:
    print(matchObj.group())
else:
    print("No match!")

