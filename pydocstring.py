class DocString():
    ''' python docstring object, apply PEP-257 docstring style checking '''

    def __init__(self, doc=""):
        ''' (DocString, str) -> None
        Initialize a Docstring constructor.

        Note: we have second option here, instead of taking doc, we can also take in the function object,
        then save the doc by calling func.__doc__, so that we have kept both docstring and function itself for reference
        '''
        self.doc = doc
        self._doc_list = self.doc.split('\n')  # if successfully parsed docstring, this eventually become empty list
        self._type_contract = TypeContract(self._type_contract_parser())
        self._description = ''
        self._requirement = ''
        self._examples = ''  # maybe not needed.

    def __str__(self):
        return self.doc

    def get_type_contract(self):
        ''' (Docstring) -> TypeContract
        Return the TypeContract object
        '''
        return self._type_contract

    def get_description(self):
        ''' (Docstring) -> Description
        Return the Description object
        '''
        return self._description

    def get_requirement(self):
        ''' (Docstring) -> Requirement
        Return the Requirement object
        '''
        return self._requirement

    def _type_contract_parser(self):
        tc = ''.join(list(filter(lambda d: '(' in d and ')' in d and '->' in d, self._doc_list)))
        self._doc_list.remove(tc)
        return tc


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
