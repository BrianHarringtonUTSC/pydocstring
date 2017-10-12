# PyDocString
`pydocstring` is a tool used to parse a function and its docstring for further marking. It extracts features from the docstring including:

- TypeContract
- Description
- Requirements
- Examples


## Example of a Design Recipe function:

```python
def divide(numerator, denominator):
    ''' (float, float) -> float
    # This is a function that divides one number by the other.
    REQ: denominator != 0
    >>> divide(1, 2)
    0.5
    >>> divide(2, 2)
    1.0
    '''
    # Get the quotient of the division.
    quotient = numerator / denominator
    # Return the quotient
    return quotient
```
