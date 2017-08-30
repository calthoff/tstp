

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
