# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

def bottles_of_beer(bob):
    """ Prints 99 Bottle of Beer on the Wall lyrics.
    :param bob: Must be a positive integer.
    """
    if bob < 1:
        print("No more bottles of beer on the wall. No more bottles of beer.")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall. {} bottles of beer. Take one down, pass it around, {}
          bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob)


bottles_of_beer(99)
