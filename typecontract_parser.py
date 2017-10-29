from parsy import *

def flatten(container):
    for i in container:
        if isinstance(i, (list, tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

@generate
def LIST():
    return (yield string("list of ") + ARG)

@generate
def SET():
    return (yield string("set of ") + ARG)

@generate
def TUPLE():
    result = (yield seq(string("tuple of ") << optional_lparen,
              optional_whitespace >> ARG.many().sep_by(regex(r',\s*')) <<
              (optional_whitespace + optional_rparen)))
    return "".join(list(flatten(result)))

@generate
def DICT():
    pair = ((ARG << optional_whitespace) +  string(":") +
               (optional_whitespace >> ARG)).many().sep_by(regex(r',\s*'))
    result = (yield seq(string("dict of {") << optional_whitespace) +
              pair +  seq(optional_whitespace >> string("}")))
    return (list(flatten(result)))

@generate
def INPUT():
    result = (yield (optional_whitespace + lparen) >>
              ARG.many().sep_by(regex(r',\s*')) << rparen)
    return list(flatten(result))

@generate
def OUTPUT():
    result = (yield seq(optional_whitespace, optional_lparen) >>
              ARG.many().sep_by(regex(r',\s*')) <<
              seq(optional_whitespace, optional_rparen))
    return list(flatten(result))

@generate
def TC():
    inputs = yield INPUT
    yield (optional_whitespace + ARROW + optional_whitespace)
    outputs = yield OUTPUT
    return {'inputs': inputs, 'outputs': outputs}

optional_whitespace = regex(r'\s*')
optional_lparen = regex(r'\(?')
optional_rparen = regex(r'\)?')
lparen = string("(")
rparen = string(")")
TYPE = regex(r'\b[a-z|A-z]+\b')
ARG = LIST | SET | TYPE
ARROW = regex(r'[-|=]+>')

## TO-DO

# Re-create the type contract parser to follow better/more well defined rules