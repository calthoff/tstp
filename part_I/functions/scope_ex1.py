# IF YOU ARE READING THIS YOU ARE READING
# AN OUTDATED VERSION OF THE BOOK. THE NEW VERSION
# IS MUCH BETTER.
# I am working with Amazon to resolve this.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

x = 100
print("scope 1")
print(x)


def f():
    y = 200
    print("scope 2")
    print(x)

f()

""" if you try to use y where this comment is, you will get an
error. """
