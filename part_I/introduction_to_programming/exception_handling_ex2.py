a = input("type a number")
b = input("type another number")
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero. Try again.")
