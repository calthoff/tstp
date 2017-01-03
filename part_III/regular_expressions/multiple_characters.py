IF YOU ARE READING THIS YOU ARE READING
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

import re

sentence = "Two is a number and too is not."

match = re.findall("t[ow]o", sentence, re.IGNORECASE)
print(match)
