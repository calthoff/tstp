# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

class Orange():
    def __init__(self):
        """all weights are in oz"""
        self.weight = 6
        self.color = 'orange'
        self.mold = 0

    def rot(self, days, temperature):
        self.mold = days * (temperature * .1)


orange = Orange()
print(orange.mold)
orange.rot(10, 98)
print(orange.mold)
