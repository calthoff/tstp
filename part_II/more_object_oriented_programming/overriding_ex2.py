class StringCount:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return self.string

    def __add__(self, other):
        return len(other.string) + len(self.string)

s1 = StringCount('Hello')
s2 = StringCount('World')

print(s1)
print(s2)
print(s1 + s2)
