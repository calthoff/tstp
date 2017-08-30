

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
