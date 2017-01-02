# IF YOU ARE READING THIS YOU ARE READING
# AN OUTDATED VERSION OF THE BOOK. THE NEW VERSION
# IS MUCH BETTER.
# I am working with Amazon to resolve this.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

try:
    a = input("type a number")
    b = input("type another number")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("b cannot be zero and a and b must be numbers. Try again.")
