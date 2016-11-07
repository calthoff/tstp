def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)
