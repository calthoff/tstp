
try:
    a = input("type a number")
    b = input("type another number")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("b cannot be zero and a and b must be numbers. Try again.")
