"""Demonstrates working with lists.
"""


#%%
def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    l1 = ['Mick', 'Keith', 'Brian', 'Charlie', 'Bill', 'Ron', 1962, True]
    # print(l1[:2])
    # print(l1 == ['Mick', 'Keith', 'Brian', 'Charlie', 'Bill', 'Ron', 1962, True])
    # print(l1 is ['Mick', 'Keith', 'Brian', 'Charlie', 'Bill', 'Ron', 1962, True])
    # print(l1 + ['The Rolling Stones', 'OK'])

    for e in l1:
        print(e)


#%%
# Test demonstrate_lists()
demonstrate_lists()


#%%
def demonstrate_list_methods():
    """Using
    append()
    insert()
    remove()
    pop()
    extend()
    count()
    index()
    reverse()
    len()
    ...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    l1 = ['Mick', 'Keith', 'Brian', 'Charlie', 'Bill', 'Ron', 1962, True]
    print(l1.append('The Rolling Stones'))
    print(l1)
    print()

    print(l1.insert(2, 'Mick Taylor'))
    print(l1)
    print()

    print(l1.pop(2))
    print(l1)
    print()

    print('Mick Taylor' in l1)
    print('Mick Taylor' not in l1)
    print()

    print(l1.count('Keith'))
    print()

    print(l1.index('Keith'))
    # print(l1.index('Keith', 3, 5))
    print()


#%%
# Test demonstrate_list_methods()
demonstrate_list_methods()

#%%


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    a = array('i', [1, 2, 3, 4])
    print(a)
    print(type(a))
    for i in a:
        print(i)


#%%
# Test demonstrate_arrays()
demonstrate_arrays()

#%%


def populate_empty_list():
    """Creating an empty list and populating it with random values
    using random.seed() and random.randint()
    """

    from random import seed, randint
    l = []
    for i in range(10):
        l.append(randint(10, 20))
    print(l)


#%%
# Test populate_empty_list()
populate_empty_list()

#%%


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """

    l1 = ['Mick', 'Keith', 'Brian', 'Charlie', 'Bill', 'Ron', 1962, True]
    l2 = l1
    print(l2 is l1)
    l2 = l1.copy()
    print(l2 is l1)


#%%
# Test duplicate_list()
duplicate_list()

#%%


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over a list of strings
    - list comprehension with enumerate(), to find indices of all occurrences of an element in a list
    Using str() and join() in printing results.
    """

    songs = ['Angie', 'No Expectations', 'Gimme Shelter', 'Ruby Tuesday', 'You Can\'t Always Get What You Want']

    # Step by step

    # l = [song for song in songs if 'a' in song]
    # print(l)
    # print()
    #
    # fw = [song.split()[0] for song in songs]
    # print(fw)
    # print()
    #
    # result = ''.join([w[0] for w in fw]).capitalize()
    # print(result)

    # All in one step

    print(''.join([t[0] for t in songs]).capitalize())

    songs = ['Angie', 'No Expectations', 'Gimme Shelter', 'Angie', 'Ruby Tuesday', 'Angie', 'You Can\'t Always Get What You Want']

    # angie_positions = list(enumerate(songs))
    # print(angie_positions)
    angie_positions = [t[0] for t in list(enumerate(songs)) if t[1] == 'Angie']
    print(angie_positions)


#%%
# Test demonstrate_list_comprehension()
demonstrate_list_comprehension()

