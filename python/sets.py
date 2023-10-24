"""Demonstrates sets.
"""


#%%
def demonstrate_sets():
    """Creating and using sets.
    - create a set and make an attempt to duplicate items (add(), update())
    - demonstrate some typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    the_rolling_stones = {'Mick', 'Keith', 'Brian', 'Bill', 'Charlie'}
    print(type(the_rolling_stones))
    print(the_rolling_stones)
    print()

    the_rolling_stones.add('Mick')
    print(the_rolling_stones)
    the_rolling_stones.add('Mick Taylor')
    print(the_rolling_stones)
    print()

    the_rolling_stones.update(['Ron', 'Bill'])
    print(the_rolling_stones)
    print()

    print(the_rolling_stones & {'Mick', 'Ron', 'Andrew'})
    print(the_rolling_stones | {'Mick', 'Ron', 'Andrew'})
    print(the_rolling_stones - {'Mick', 'Ron', 'Andrew'})
    print(the_rolling_stones ^ {'Mick', 'Ron', 'Andrew'})


#%%
# Test demonstrate_sets()
demonstrate_sets()


