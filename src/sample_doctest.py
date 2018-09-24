# sample_doctest.py
# Using unit tests included in docstrings 

def pow_of_two(x):
    """Return x to the power of 2.

    >>> pow_of_two(4)
    16
    >>> pow_of_two(-2)
    4
    """
    return x**2

def float_div_by_two(x):
    """Return x divided by 2 in floating point precision.

    >>> float_div_by_two(49)
    24.5
    >>> float_div_by_two(48)
    24.0
    """
    return x / 2.0

def get_evens(n):
    """Return the first n even numbers as a list.
    
    >>> get_evens(10)
    [0, 2, 4, 6, 8]
    >>> get_evens(7)
    [0, 2, 4, 6]
    """
    return list(range(0, n, 2))

def get_mid(data):
    """Return the midpoint value in data.
    
    >>> get_mid([1,2,3,4,5])
    3
    >>> get_mid(['a','b','c','d','e','f','g'])
    'd'
    """
    return data[len(data)//2]

def get_last_half(data):
    """Return the values in the last half of data (slice) as a list.
    
    >>> get_last_half([1,2,3,4,5,6])
    [4, 5, 6]
    >>> get_last_half(['a','b','c','d','e','f','g'])
    ['d', 'e', 'f', 'g']
    """
    return data[len(data)//2:]
