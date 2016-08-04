import re

line = """__yellow__ __red__ and __blue__ are colors"""

matchObj = re.findall('__.*?__', line)

if matchObj:
    print matchObj
else:
    print("No match!")
