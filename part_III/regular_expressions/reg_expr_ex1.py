import re

line = "Match this."

matchObj = re.findall('this', line)

if matchObj:
    print(matchObj.group())
else:
    print("No match!")

