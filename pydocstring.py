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


if __name__ == "__main__":
    def func1(a_str, a_int, a_float, a_list, a_dict):
        ''' (str, int, float, list of str, dict of {str: int}) -> bool
        This is a sample doc, this line is not too long.
        This line is a bit longer than expected, we need to break this
        line into two.

        REQ: this is a requirement
        REQ: another requirement
        requirement: possibly another requirement like this

        >>> func1('a', 1, 0.8, ['hello', 'world'], {'hi': 8})
        True
        >>> func1('a', 1, 0.8, ['hello', 'world'], {'hi': 9})
        False
        '''
        return False  # dummy code


    def func2(a_str, a_int, a_float, a_list, a_dict):
        ''' (str, int, float, list of str, dict of {str: int}) -> bool
        REQ: this is a requirement
        REQ: another requirement
        requirement: possibly another requirement like this

        This is another sample doc, this possibly requirements stated before description.
        This line is a bit longer than expected, we need to break this
        line into two.

        >>> func2('a', 1, 0.8, ['hello', 'world'], {'hi': 8})
        True
        >>> func2('a', 1, 0.8, ['hello', 'world'], {'hi': 9})
        False
        '''
        return False  # dummy code


    print(func1.__doc__)
    print(func2.__doc__)
