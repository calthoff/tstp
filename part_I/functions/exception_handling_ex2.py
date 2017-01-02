# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK. THE NEW VERSION
# IS MUCH BETTER.
# I am working with Amazon to resolve this.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version


a = input("type a number")
b = input("type another number")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")
