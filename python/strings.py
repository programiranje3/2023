"""Demonstrates working with strings in Python.
"""

import string

import settings
import util.utility


#%%
def demonstrate_formatting():
    """Demonstrating details of string formatting.
    - using classical formatting
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    # print('Mick and Keith have been born in %s, in %d.' % ('Dartford', 1943))
    # print('C:\nobody')
    # print(r'C:\nobody')
    # print("""You Can\'t Always Get
    # What You Want""")
    # print('Mick and Keith\t' * 3)
    # mk = 'Mick and Keith'
    # print(mk[5:])
    # print(mk[-5:])
    print(str('Mick and Keith\t'))
    print(repr('Mick and Keith\t'))


#%%
# Test demonstrate_formatting()
demonstrate_formatting()

#%%


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('{0} and {1} have been born in {2}, in {3}'.format('Mick', 'Keith', 'Dartford', 1943))
    print('{1} and {0} have been born in {2}, in {3}'.format('Mick', 'Keith', 'Dartford', 1943))


#%%
# Test demonstrate_fancy_formatting()
demonstrate_fancy_formatting()

#%%


def demonstrate_fancy_formatting_with_f_strings():
    """Using f-strings in formatting.
    - format strings like f'Some text {some var}, more text {another var}...', etc.
    """

    mick = 'Mick Jagger'
    keith = 'Keith Richards'
    print(f'{mick} and {keith} have been born in 1943.')
    print()

    from datetime import date
    d1 = date(1943, 12, 18)

    print(f'{keith} has been born on {util.utility.format_date(d1)}.')


#%%
# Test demonstrate_fancy_formatting_with_f_strings()
demonstrate_fancy_formatting_with_f_strings()

#%%


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals()), len(), ..., strip() (lstrip(), rstrip())
    """

    keith = 'Keith Richards'
    print(keith.endswith('Richards'))
    print(keith.startswith('Keith'))
    print(keith.split())
    print(keith.split('th'))
    print(keith.center(50, '*'))
    print('Rich' in keith)
    print('Keith Richards' == keith)
    print(len(keith))
    print('           Keith          '.strip())
    print('           Keith          '.rstrip(), 'and Mick Jagger')


#%%
# Test demonstrate_string_operations()
demonstrate_string_operations()
