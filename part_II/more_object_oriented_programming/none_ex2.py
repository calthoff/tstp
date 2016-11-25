class Triangle(object):
    def __eq__(self, other):
        return True

triangle = Triangle()
print(triangle == None)
print(triangle is None)
