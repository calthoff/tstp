# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

class PublicPrivateExample:
    def __init__(self):
        self.public_variable = "callers know they can access this"
        self._dontusethisvariable = "callers know they shouldn't access this"

    def _dont_use_this_method(self):
        # callers know they shouldn't use this method
        pass

    def public_method(self):
        # callers know they can use this method
        pass
