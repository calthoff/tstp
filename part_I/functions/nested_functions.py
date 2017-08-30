

def f():
    print("Inner Function!")

    def x():
        print("Nested Function!")

    x()

f()
