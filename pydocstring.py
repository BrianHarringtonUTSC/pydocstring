class DocString:
    """ python docstring object, apply PEP-257 docstring style checking """

    def __init__(self, func):
        """ (DocString, str) -> None
        Initialize a DocString constructor.

        Note: we have second option here, instead of taking doc, we can also
        take in the function object,
        then save the doc by calling func.__doc__, so that we have kept both
        docstring and function itself for reference
        """
        self.doc = func.__doc__
        self._doc_list = list(map(str.strip, self.doc.split('\n')))
        # if successfully parsed docstring, this^ eventually becomes empty list
        self._type_contract = self._parse_type_contract()
        self._inline_type_contract = self._parse_inline_type_contract(func)
        self._description = self._parse_description()
        self._requirements = self._parse_requirements()
        self._examples = self._parse_examples()

    def _parse_inline_type_contract(self, func):
        type_list = list(func.__annotations__.values())
        inputs = type_list[0:-1]
        outputs = type_list[-1]
        return TypeContract(inputs, outputs)

    def __str__(self):
        return self.doc

    def get_type_contract(self):
        """ (DocString) -> TypeContract
        Return the TypeContract object
        """
        return self._type_contract

    def get_inline_type_contract(self):
        return self._inline_type_contract

    def get_description(self):
        """ (DocString) -> Description
        Return the Description object
        """
        return self._description

    def get_requirement(self):
        """ (DocString) -> Requirement
        Return the Requirement object
        """
        return self._requirement

    def _parse_type_contract(self):
        """ (DocString) -> TypeContract
        Returns the type contract of the given docstring
        """
        # get the type contract as a string
        type_contract = ''.join(list(
            filter(lambda d: '(' in d and ')' in d and '->' in d,
                   self._doc_list)))
        # determine where the inputs and output start in the string
        input_start, input_end = type_contract.find(
            "(") + 1, type_contract.find(")")
        output_start = type_contract.find(
            "->") + 2 if "->" in type_contract else type_contract.find(
            "-->") + 3
        # split the inputs by the comma, and remove any extra white space
        inputs = [token.strip() for token in
                  type_contract[input_start:input_end].split(",")]
        outputs = []
        outputs_str = type_contract[output_start:]
        if "(" in outputs_str and ")" in outputs_str:
            # if parentheses are present in the outputs, remove them but
            # only one
            # occurrence. If they put too many brackets they should remain
            # in the final output
            outputs_str = outputs_str.replace("(", "", 1)
            outputs_str = outputs_str.replace(")", "", 1)
        # split the outputs string by commas and iterate through each token,
        #  removing
        # extra whitespace and matching parentheses if present
        for token in outputs_str.split(","):
            token = token.strip()
            outputs.append(token)
        return TypeContract(inputs, outputs)

    def _parse_requirements(self):
        """ (DocString) -> Requirement
        Parses a given string (docstring) and extracts the description.
        """
        # Search for the beginning "req" case-insensitively
        requirements_list = []
        for item in self._doc_list:
            if item[0:3].lower() == "req":
                requirements_list.append(item)

        return Requirement(requirements_list)

    def _parse_description(self):
        """ (DocString) -> Description
        Parses a given string (docstring) and extracts the requirements.
        """
        return Description(None)

    def _parse_examples(self):
        """ (DocString) -> Example
        Parses a given string (docstring) and extracts the examples.
        """
        return Example(None)


class TypeContract:
    def __init__(self, arg_types, return_types):
        # Type contract should contain the arguments and return types
        self._arg_types = arg_types
        self._return_types = return_types

    def __eq__(self, other):
        return False


class Description:
    def __init__(self, text):
        self._text = text

    def __eq__(self, other):
        # Checking for exact match naively, can be changed later.
        return self._text == other.text


class Requirement:
    def __init__(self, requirements):
        # DocString can have multiple requirements.
        self._requirements = requirements

    def __eq__(self, other):
        return False


class Example:
    def __init__(self, examples):
        self._examples = examples

    def __eq__(self, other):
        return False


if __name__ == "__main__":
    def func1(a_str, a_int, a_float, a_list, a_dict):
        """ (str, int, float, DocString, dict of {str: int}) -> (bool)
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
        """
        return False  # dummy code


    def func2(a_str, a_int, a_float, a_list, a_dict):
        """(str, int, float, DocString, dict of {str: int}) -> (bool, float,
        list of int)
        REQ: this is a requirement
        REQ: another requirement
        requirement: possibly another requirement like this

        This is another sample doc, this possibly requirements stated before
        description.
        This line is a bit longer than expected, we need to break this
        line into two.

        >>> func2('a', 1, 0.8, ['hello', 'world'], {'hi': 8})
        True
        >>> func2('a', 1, 0.8, ['hello', 'world'], {'hi': 9})
        False
        """
        return False  # dummy code

doc = DocString(func1)
print(doc._requirements._requirements)
print(doc._examples._examples)
print(str(doc.get_type_contract()))
doc2 = DocString(func2)
doc2_tc = doc2.get_type_contract()
print(doc2_tc)
