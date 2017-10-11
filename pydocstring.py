class DocString():
    def __init__(self):
        self._type_contract = ''
        self._description = ''
        self._requirement = ''
        self._examples = ''  # maybe not needed.


class TypeContract():
    def __init__(self):
        self._arg_types = []
        self._return_types = []

    def __eq__(self, other):
        return False


class Description():
    pass


class Requirement():
    pass


class Example():
    pass
