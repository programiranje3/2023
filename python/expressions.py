"""Demonstrates how operators and expressions work in Python.
"""

from settings import *


#%%
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    Arithmetic operators in Python are pretty much the same as in other programming languages.
    The integer division operator: //
    """

    print(22 // 17 + 38 % 5 - 2)


#%%
# Test demonstrate_arithmetic_operators()
demonstrate_arithmetic_operators()

#%%


def demonstrate_relational_operators():
    """Working with relational operators.
    - simple comparisons
    - comparing dates (== vs. is)
    - comparing dates (>, <, etc. with dates)
    - None in comparisons, type(None)
    """

    # print(3 > 5)
    # print()
    #
    # if 3 > 5:
    #     print(True)
    # else:
    #     print(False)
    # print()
    #
    # if '':
    #     print(True)
    # else:
    #     print(False)
    # print()

    from datetime import date
    d1 = date(1943, 12, 18)
    d2 = date(1943, 7, 26)

    # if d1 > d2:
    #     print(True)
    # else:
    #     print(False)
    # print()
    #
    # print(id(d1))
    # print(id(d2))
    # print()
    #
    # d3 = date(1943, 7, 26)
    # print(d2 == d3)
    # print(d2 is d3)
    # print(d3 is date(1943, 7, 26))
    # print()

    print(type(None))
    print(d1 == None)
    print(d1 > None)


#%%
# Test demonstrate_relational_operators()
demonstrate_relational_operators()

#%%


def demonstrate_logical_operators():
    """Working with logical operators.
    - logical operations with True, False and None
    - logical operations with dates
        - make sure to read this: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not !!!
          (or just this: https://stackoverflow.com/questions/44612144/logical-operators-in-python)
    - logical operations with None (incl. None and int, None and date, etc.)
    - None and date vs. None > date
    """

    from datetime import date
    d1 = date(1943, 12, 18)
    d2 = date(1943, 7, 26)

    # print((2 > 1) and (2 < 5))
    # print(2 and 5)
    # print('' and 0)
    # print(2 and 0)

    print({1} or None)


#%%
# Test demonstrate_logical_operators()
demonstrate_logical_operators()

