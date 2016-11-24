class Foo(object):
    def __eq__(self, other):
        return True

foo = Foo()
print(foo == None)
print(foo is None)

