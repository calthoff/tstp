# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

import re

line = """The numbers 172 can be found on the back of the U.S. $5 dollar bill in the bushes at the base
       of the Lincoln Memorial."""

matchObj = re.findall('\d+', line)

if matchObj:
    print(matchObj)
else:
    print("No match!")
