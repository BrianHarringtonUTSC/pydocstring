from typecontract_parser import *

class DocString():
    ''' python docstring object, apply PEP-257 docstring style checking '''

    def __init__(self, function):
        ''' (DocString, str) -> None
        Initialize a DocString constructor.

        Note: we have second option here, instead of taking doc, we can also take in the function object,
        then save the doc by calling func.__doc__, so that we have kept both docstring and function itself for reference
        '''
        self.doc = function.__doc__
        self._doc_list = list(map(str.strip, self.doc.split('\n')))  # if successfully parsed docstring, this eventually become empty list
        self._type_contract = self._parse_type_contract()
        self._description = self._parse_description()
        self._requirements = self._parse_requirements()
        self._examples = self._parse_examples()

    def __str__(self):
        return self.doc

    def get_type_contract(self):
        ''' (DocString) -> dict of {str: list of str}
        Return the TypeContract object
        '''
        return self._type_contract

    def get_description(self):
        ''' (DocString) -> Description
        Return the Description object
        '''
        return self._description

    def get_requirement(self):
        ''' (DocString) -> list of str
        Return the Requirement object
        '''
        return self._requirements

    def get_examples(self):
        '''(DocString) -> Example
        Return the Example object
        '''

    def _parse_type_contract(self):
        ''' (DocString) -> dict of {str: list of str}
        Returns a dictionary that contains 2 lists: a list of input types and
        a list of output types
        '''
        result = TC.parse_partial(self.doc)[0]
        return TypeContract(result["inputs"], result["outputs"])

    def _parse_requirements(self):
        ''' (DocString) -> list of str
        Parses a given string (docstring) and extracts the description.
        '''
        # Search for the beginning "req" case-insensitively
        requirements_list = []
        for item in self._doc_list:
            if item[0:3].lower() == "req":
                requirements_list.append(item)

        return requirements_list

    def _parse_description(self):
        ''' (DocString) -> Description
        Parses a given string (docstring) and extracts the requirements.
        '''
        return "Pending Description"

    def _parse_examples(self):
        ''' (DocString) -> Example
        Parses a given string (docstring) and extracts the examples.
        '''
        return Example(None)

class TypeContract:
    def __str__(self) -> str:
        return "inputs: {}, outputs: {}".format(self._arg_types,
                                                 self._return_types)

    def __init__(self, arg_types, return_types):
        # Type contract should contain the arguments and return types
        self._arg_types = arg_types
        self._return_types = return_types

    def __eq__(self, other):
        return False

class Description():
    def __init__(self, text):
        self._text = text

    def __eq__(self, other):
        # Checking for exact match naively, can be changed later.
        return self._text == other.text


class Requirement():
    def __init__(self, requirements):
        # DocString can have multiple requirements.
        self._requirements = requirements

    def __eq__(self, other):
        return False


class Example():
    def __init__(self, examples):
        self._examples = examples

    def __eq__(self, other):
        return False


if __name__ == "__main__":
    def func1(a_str, a_int, a_float, a_list, a_dict):
        ''' (str, int, float, list of str) -> (bool)
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
        ''' (str, int, float, list of str) -> (bool, float, list of int)
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

    doc = DocString(func1)
    print(doc.get_type_contract())
    doc = DocString(func2)
    print(doc.get_type_contract())

