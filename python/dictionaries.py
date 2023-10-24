"""Demonstrates dictionaries.
From: https://qr.ae/TWCAvj:
Python uses dictionaries all over the place:
- the variables and functions in a module - stored in a dictionary  # can be shown using globals()
- the local variables in a function - stored in a dictionary        # can be shown using locals(); see functions.py
- the implementation of a function - a dictionary
- a class is a dictionary
- an instance of a class is another dictionary
- the modules your program has imported - you guessed it - another dictionary
- even Python set objects are implemented as modified dictionaries
To paraphrase Tim Peter's 'Zen of Python': "dictionaries are great - let's do more of them".
Read more at https://qr.ae/TWCAvj.
"""


#%%
def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - access dictionary values by the corresponding keys (syntax: value = d[key])
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    # mick = {}
    # print(type(mick))
    # print(mick)
    # print()

    glimmer_twins = {'mick': 'Mick Jagger', 'keith': 'Keith Richards', 'birth_year': 1943}
    print(glimmer_twins)
    print()

    # mick = glimmer_twins['mick']
    # print(mick)
    # print()

    # # print(glimmer_twins.items())
    # for k, v in glimmer_twins.items():
    #     print(k + ':', v)
    # print()

    # from pprint import pprint
    # pprint(glimmer_twins, width=1)
    # print()

    glimmer_twins['band'] = 'The Rolling Stones'
    # print(glimmer_twins.items())
    # print(glimmer_twins)
    # print()

    # del glimmer_twins['band']
    # print(glimmer_twins)
    # print()

    other = {'age': 80, 'city': 'Dartford'}
    songs = [('angie', 'Angie'), ('no_expectations', 'No Expectations')]

    # # glimmer_twins.update(other)
    # # print(glimmer_twins)
    # # print()
    # # glimmer_twins.update(songs)
    # # # glimmer_twins.update([('other', other)])        # not possible, in update() the v in (k, v) must be str or int
    # glimmer_twins['other'] = other
    # print(glimmer_twins)
    # print(glimmer_twins['other']['age'])
    # print()

    print(glimmer_twins.keys())
    print(glimmer_twins.values())


#%%
# Test demonstrate_dictionaries()
demonstrate_dictionaries()


#%%
def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # if by == 'k' or by == 'K':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # if by == 'v' or by == 'V':
    #     return dict(sorted(zip(d.values(), d.keys())))
    # return None

    # from operator import itemgetter
    #
    # if by == 'k' or by == 'K':
    #     return dict(sorted(d.items(), key=itemgetter(0)))
    # if by == 'v' or by == 'V':
    #     return dict(sorted(d.items(), key=itemgetter(1)))
    # return None

    if by == 'k' or by == 'K':
        return dict(sorted(d.items(), key=lambda x: x[0]))
    if by == 'v' or by == 'V':
        return dict(sorted(d.items(), key=lambda x: x[1]))
    return None


#%%
def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    from pprint import pprint

    songs = {2: 'Angry', 1: 'Brown Sugar', 3: 'Jumpin\' Jack Flash'}
    glimmer_twins = {'mick': 'Mick Jagger', 'keith': 'Keith Richards', 'birth_year': 1943}
    glimmer_twins = {'mick': 'Mick Jagger', 'keith': 'Keith Richards', 'birth_year': '1943'}

    # pprint(sort_dictionary(songs, by='k'))
    # pprint(sort_dictionary(songs, by='v'))
    # pprint(sort_dictionary(songs, by='d'))
    pprint(sort_dictionary(glimmer_twins, by='k'))
    pprint(sort_dictionary(glimmer_twins, by='v'))
    pprint(sort_dictionary(glimmer_twins, by='d'))


#%%
# Test demonstrate_dict_sorting()
demonstrate_dict_sorting()

