"""Demonstrates tuples.
"""


#%%
def demonstrate_tuples():
    """Creating and using tuples.
    - create and print empty tuple, 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    the_kinks = ()
    print(type(the_kinks))
    print(the_kinks)
    print()

    mick = 'Mick',
    print(mick)
    print()

    glimmer_twins = ('Mick', 'Keith', )
    print(glimmer_twins)
    print()

    the_rolling_stones = ('Mick', 'Keith', 'Ron')
    print(the_rolling_stones)
    print()

    sticky_fingers = ('The Rolling Stones', 1971, True)
    print(sticky_fingers)
    print()

    print(sticky_fingers[1])
    print()

    # sticky_fingers[1] = 1972


#%%
# Test demonstrate_tuples()
demonstrate_tuples()


#%%
def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    the_rolling_stones = 'Mick', 'Keith', 'Ron'
    print(type(the_rolling_stones))
    print(the_rolling_stones)
    print()

    mick, keith, ron = the_rolling_stones
    print(mick, keith, ron)
    print({mick, keith, ron})
    print(type({mick, keith, ron}))


#%%
# Test demonstrate_packing()
demonstrate_packing()


#%%
def demonstrate_zip():
    """Using the built-in zip() function with tuples and multi-counter for-loop.
    - demonstrate zip object
    - demonstrate converting a zip object to a list object
    - demonstrate that a zip object is an iterator (must be re-initialized after looping)
    """

    members = ('Mick Jagger', 'Keith Richards', 'Bill Wyman', 'Charlie Watts', 'Brian Jones')
    birth_years = (1940, 1942, 1936, 1941, 1942)
    birth_places = ('Dartford', 'Dartford', 'London', 'London', 'Cheltenham')

    the_rolling_stones = zip(members, birth_years, birth_places)
    print(the_rolling_stones)
    print(list(the_rolling_stones))
    print()

    the_rolling_stones = zip(members, birth_years, birth_places)    # iterator, must be re-initialized
    for m, y, p in the_rolling_stones:
        print(m + ':', p + ',', y)
    print()


#%%
# Test demonstrate_zip
demonstrate_zip()

