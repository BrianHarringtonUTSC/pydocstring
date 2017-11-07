import parsy as p


def flatten(container):
    """(list) -> generator
    Returns a generator object that once converted into a list, contains the same
    elements as the inputted list but without any of the nesting.
    """
    for i in container:
        if isinstance(i, list):
            for j in flatten(i):
                yield j
        else:
            yield i


# recursively define how a list can be represented
@p.generate("list of the form 'list[ of type[ or type]]'")
def _list():
    """() -> Parser
    A parser defined recursively to handle the occurrences of lists in
    the type contract.
    """
    # first define how our arguments can look (list, list of int,
    # list of str or int, etc)
    union_args = (_argument + whitespace + union + whitespace + _argument
                  # this is to ensure that if a student uses a union but doesn't
                  #  complete it, it still appears in the output
                  | _argument + whitespace + union + optional_whitespace)
    # then declare the forms of lists that are accepted (including recursive definitions)
    token = (p.string("list of") + whitespace + union_args
             | p.string("list of") + whitespace + _argument
             | p.string("list"))
    return (yield token)


# recursively define how a tuple can be represented
@p.generate("tuple of the form 'tuple[ of type[ or type]]'")
def _tuple():
    """() -> Parser
    """
    union_args = (_argument + whitespace + union + whitespace + _argument
                  # this is to ensure that if a student uses a union but doesn't
                  #  complete it, it still appears in the output
                  | _argument + whitespace + union + optional_whitespace)
    # then declare the forms of tuples that are accepted (including recursive definitions)
    token = (p.string("tuple of") + whitespace + union_args
             | p.string("tuple of") + whitespace + _argument
             | p.string("tuple"))
    return (yield token)


# recursively define how a tuple can be represented
@p.generate("set of the form 'set[ of type[ or type]]'")
def _set():
    """() -> Parser
    """
    union_args = (_argument + whitespace + union + whitespace + _argument
                  # this is to ensure that if a student uses a union but doesn't
                  #  complete it, it still appears in the output
                  | _argument + whitespace + union + optional_whitespace)
    # then declare the forms of sets that are accepted (including recursive definitions)
    token = (p.string("set of") + whitespace + union_args
             | p.string("set of") + whitespace + _argument
             | p.string("set"))
    return (yield token)


# recursively define how a tuple can be represented
@p.generate("dict of the form 'dict of {type:type}'")
def _dict():
    """() -> Parser
    """
    # declare the forms of dicts that are accepted (including recursive definitions)
    # union of dicts is not accepted
    token = (p.string("dict of") + whitespace + l_curl_brack + optional_whitespace + _argument
             + optional_whitespace + colon + optional_whitespace + _argument + optional_whitespace + r_curl_brack
             | p.string("dict"))
    return (yield token)


@p.generate("Argument of the for type or type")
def _union():
    """
    () -> Parser
    """
    arg = (_list | _tuple | _set | _dict | _type)
    token = (arg + whitespace + union + whitespace + arg
             # this is to ensure that if a student uses a union but doesn't
             | arg + whitespace + union + optional_whitespace)
    return (yield token)


@p.generate("Arguments (for inputs/outputs) are not in the correct format.")
def _arguments():
    tokens = _argument.many().sep_by(optional_whitespace + comma + optional_whitespace)
    return (yield tokens)


@p.generate("Type contract does not follow the expected format. "
            + "Check your arguments and make sure they are correctly formatted")
def _type_contract():
    yield optional_whitespace
    params = yield _params
    yield (whitespace + _arrow + whitespace)
    returns = yield _returns
    return [list(flatten(params)), list(flatten(returns))]


def parse(docstring):
    """(DocString) -> TypeContract
    Returns a TypeContract object containing the inputs and outputs of the
    specified function.
    """
    data = docstring.doc.replace("\n", " ")
    results = _type_contract.parse_partial(data)[0]
    return results


# define whitespaces
whitespace = p.regex(r'\s+').desc("whitespace")
optional_whitespace = p.regex(r'\s*').desc("optional whitespace")

# define different types of brackets
l_paren = p.string("(")
r_paren = p.string(")")
optional_l_paren = p.regex(r'\(?')
optional_r_paren = p.regex(r'\)?')
l_curl_brack = p.string("{")
r_curl_brack = p.string("}")

# colon, comma, and union
colon = p.string(":")
comma = p.string(',')
union = p.string("or")

# Basic single-word data-types (str, int, TypeContract, etc)
_type = p.regex(r'\b([a-z]|[A-Z]|\.)+\b').desc("data-type")
_arrow = p.regex(r'[-|=]+>')
# One collective definition of arguments
_argument = (_list | _tuple | _set | _dict | _union | _type)
# declare how our params should look
_params = (l_paren + optional_whitespace).map(list) >> _arguments << (optional_whitespace + r_paren).map(list)
# declare how the returns should look like
_returns = optional_l_paren.map(list) >> _arguments << optional_r_paren.map(list)
