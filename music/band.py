"""The class representing the concept of a music group/band.
It includes a list of Musician objects (band members) and the date when the band started performing together.

The corresponding exception classes are included as well.
File I/O and JSON encoding/decoding of Band objects are demonstrated too.
"""


#%%
# Setup / Data

import pickle
from datetime import date, datetime, time
# import json
import sys

# from music.musician_module import Musician
from util.utility import format_date, get_project_dir, get_data_dir

from testdata.musicians import *


#%%
class Band:
    """The class describing the concept of a music group/band.
    It includes a list of Musician objects (band members)
    and the dates when the band started/stopped performing together.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as genres, date_pattern,...

    genre = ['rock \'n\' roll', 'blues', 'hip hop']

    def __init__(self, name, *members, start=date.today(), end=date.today()):

        # Code to check if the band name is specified correctly (possibly raises BandNameError)
        band_name_err = not isinstance(name, str) or not len(name)
        if band_name_err:
            raise BandNameError(name)

        self.name = name
        self.members = members
        self.start = start
        self.end = end

        # self.__i = 0                                  # introduce and initialize iterator counter, self.__i

    def __str__(self):
        n = self.name
        m = ', '.join([str(m) for m in self.members]) if self.members else ''
        s = self.start.year
        e = self.end.year
        return f'{n} ({m}), {s}-{e}' if m else f'{n} (members unknown), {s}-{e}'

    def __eq__(self, other):

        # Musician objects are unhashable, so comparing the members tuples from self and other directly does not work;
        # see https://stackoverflow.com/a/14721133/1899061, https://stackoverflow.com/a/17236824/1899061
        # return self == other if isinstance(other, Band) else False    # No! Musician objects are unhashable!
        # However, this works:
        # return self.__dict__ == other.__dict__ if isinstance(other, Band) else False

        # # members must be compared 'both ways', because the two tuples can be of different length
        # m_diff_1 = [x for x in self.members if x not in other.members]
        # m_diff_2 = [x for x in other.members if x not in self.members]
        # m = len(m_diff_1) == len(m_diff_2) == 0

        # members must be compared 'both ways', because the two tuples can be of different length

        return self.__dict__ == other.__dict__ if isinstance(other, Band) else False

    @staticmethod
    def is_date_valid(d):
        """It is assumed that a band does not perform together since more than ~60 years ago.
        So, the valid date to denote the start of a band's career is between Jan 01, 1960, and today.
        """

        return date(1954, 7, 5) < d < date.today() if isinstance(d, date) else False

    def __iter__(self):
        """Once __iter__() and __next__() are implemented in a class,
        we can create an iterator object by calling the iter() built-in function on an object of the class,
        and then call the next() built-in function on that object.
        It is often sufficient to just return self in __iter__(),
        if the iterator counter such as self.__i is introduced and initialized in __init__().
        Alternatively, the iterator counter (self.__i) is introduced and initialized here.
        """

        self.__i = 0
        return self               # sufficient if the iterator counter is introduced and initialized in __init__()

    def __next__(self):
        if self.__i < len(self.members):
            m = self.members[self.__i]
            self.__i += 1
            return m
        raise StopIteration


#%%
# Check class variables

print(Band.genre[0])


#%%
# Test the basic methods (__init__(), __str__(),...)

# the_rolling_stones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood],
#                           start=date(1962, 7, 12), end=date.today())
the_rolling_stones = Band('The Rolling Stones',
                          start=date(1962, 7, 12), end=date.today())
print(the_rolling_stones)
print(the_rolling_stones == Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood],
                                 start=date(1962, 7, 12), end=date.today()))


#%%
# Test the date validator (@staticmethod is_date_valid(<date>))

print(Band.is_date_valid(date(1962, 7, 12)))


#%%
# Test the iterator

the_rolling_stones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood],
                          start=date(1962, 7, 12), end=date.today())
i = iter(the_rolling_stones)
print(i)
print()

for _ in range(len(the_rolling_stones.members)):
    print(next(i))
# print(next(i))              # raises StopIteration, since the iterator is exhausted
print()

i = iter(the_rolling_stones)
# print(next(i))
for m in i:                 # another, very efficient way to demonstrate iterators
    print(m)
print()


#%%
def next_member(band):
    """Generator that shows members of a band, one at a time.
    yield produces a generator object, on which we call the next() built-in function.
    A great tutorial on generators: https://realpython.com/introduction-to-python-generators/.
    """

    for m in band.members:
        print(input('Next:'))
        yield m
        print('Yeah!')


#%%
# Test next_member(band)

the_rolling_stones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood],
                          start=date(1962, 7, 12), end=date.today())
g = next_member(the_rolling_stones)
# print(g)
while True:
    try:
        print(next(g))
    except StopIteration:
        break

#%%
# Demonstrate generator expressions

print((i for i in range(6)))
g = (i for i in range(6))
while True:
    try:
        print(next(g))
    except StopIteration:
        break


#%%
# Demonstrate JSON encoding/decoding of Band objects

# Using the json_tricks module from the json-tricks external package (https://github.com/mverleg/pyjson_tricks).
# From the package documentation:
# The JSON string resulting from applying the json_tricks.dumps() function stores the module and class name.
# The class must be importable from the same module when decoding (and should not have changed).
# If it isn't, you have to manually provide a dictionary to cls_lookup_map when loading
# in which the class name can be looked up. Note that if the class is imported, then globals() is such a dictionary
# (so try loads(json, cls_lookup_map=globals())).
# Also note that if the class is defined in the 'top' script (that you're calling directly),
# then this isn't a module and the import part cannot be extracted. Only the class name will be stored;
# it can then only be deserialized in the same script, or if you provide cls_lookup_map.
# That's why the following warning appears when serializing Band objects in this script:
# UserWarning: class <class '__main__.Band'> seems to have been defined in the main file;
# unfortunately this means that it's module/import path is unknown,
# so you might have to provide cls_lookup_map when decoding.

# Single object
from json_tricks import loads, dumps
the_rolling_stones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood],
                          start=date(1962, 7, 12), end=date.today())
the_rolling_stones_json = dumps(the_rolling_stones, indent=4)
print(the_rolling_stones_json)
the_rolling_stones_restored = loads(the_rolling_stones_json)
# print(type(the_rolling_stones))
# print(type(the_rolling_stones_restored))
# print(type(the_rolling_stones.members[0]))
# print(type(the_rolling_stones_restored.members[0]))
print()

# The following two lines return strings that look the same...
print(the_rolling_stones)
print(the_rolling_stones_restored)
# ... but the next one still returns False.
# Already tried the cls_lookup_map=globals() trick, but it didn't help.
# The probable explanation: the __eq__() is based on comparing __dict__s for the two objects.
# Printing these dicts reveals that the addresses of the Musician objects in the two __dict__s are different.
# comparing the contents of the Musician objects pairwise in a loop shows that they are the same.
print(the_rolling_stones == loads(the_rolling_stones_json))

# List of objects

# theBeatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
#                   start=date(1957, 7, 6), end=date(1970, 4, 10))
# theRollingStones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood, charlieWatts],
#                         start=date(1962, 7, 12))
# pinkFloyd = Band('Pink Floyd', *[sydBarrett, davidGilmour, rogerWaters, nickMason, rickWright])

# bands = [theBeatles, theRollingStones, pinkFloyd]


#%%
class BandError(Exception):
    """Base class for exceptions in this module.
    """

    pass


#%%
class BandNameError(BandError):
    """Exception raised when the name of a band is specified incorrectly.
    """

    def __init__(self, name):
        Exception.__init__(self, f"'{name}' is not a valid band name")
        self.name = name


#%%
# Demonstrate exceptions

the_rolling_stones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood],
                          start=date(1962, 7, 12), end=date.today())

#%%
# Catching exceptions - try-except block
# If an exception is caught as e, then e.args[0] is the type of exception (relevant for exception handling).
# To write error messages to the exception console, use sys.stderr.write(f'...').

try:
    for i in range(4):
        print(the_rolling_stones.members[i])
except Exception as e:
    # print(e)
    # print(f'{type(e)}: {e}')
    # print(f'{type(e).__name__}: {e}')
    # print(f'{type(e).__name__}: {e}')
    sys.stderr.write(f'\n{type(e).__name__}: {e}\n\n')

#%%
# Catching multiple exceptions and the 'finally' clause

try:
    for i in range(3):
        print(the_rolling_stones.members[i])
    print(the_rolling_stones / 5)
except IndexError as e:
    # print(e)
    # print(f'{type(e)}: {e}')
    # print(f'{type(e).__name__}: {e}')
    # print(f'{type(e).__name__}: {e}')
    # sys.stderr.write(f'\nIndexError: {e}\n\n')
    # sys.stderr.write(f'\nIndexError: {e.args}\n\n')
    sys.stderr.write(f'\nIndexError: {e.args[0]}\n\n')
except Exception as e:
    sys.stderr.write(f'\n{type(e).__name__}: {e}\n\n')
finally:
    print('That\'s it.')

#%%
# Using the 'else' clause (must be after all 'except' clauses)

try:
    for i in range(3):
        print(the_rolling_stones.members[i])
    # print(the_rolling_stones / 5)
except IndexError as e:
    # print(e)
    # print(f'{type(e)}: {e}')
    # print(f'{type(e).__name__}: {e}')
    # print(f'{type(e).__name__}: {e}')
    # sys.stderr.write(f'\nIndexError: {e}\n\n')
    # sys.stderr.write(f'\nIndexError: {e.args}\n\n')
    sys.stderr.write(f'\nIndexError: {e.args[0]}\n\n')
except Exception as e:
    sys.stderr.write(f'\n{type(e).__name__}: {e}\n\n')
else:
    print('No exception caught')
finally:
    print('That\'s it.')

#%%
# Catching 'any' exception - empty 'except' clause

try:
    for i in range(3):
        print(the_rolling_stones.members[i])
    print(the_rolling_stones / 5)
except:
    sys.stderr.write(f'\nCaught an exception\n\n')

#%%
# Catching user-defined exceptions

try:
    the_rolling_stones = Band('', *[mickJagger, keithRichards, ronWood],
                              start=date(1962, 7, 12), end=date.today())
except BandNameError as e:
    sys.stderr.write(f'\nBandNameError: {e.args[0]}\n\n')
else:
    print(the_rolling_stones)

#%%
# Demonstrate working with files

theBeatles = Band('The Beatles', *[johnLennon, paulMcCartney, georgeHarrison, ringoStarr],
                  start=date(1957, 7, 6), end=date(1970, 4, 10))
theRollingStones = Band('The Rolling Stones', *[mickJagger, keithRichards, ronWood],
                        start=date(1962, 7, 12))
pinkFloyd = Band('Pink Floyd', *[sydBarrett, davidGilmour, rogerWaters, nickMason, rickWright])

bands = [theBeatles, theRollingStones, pinkFloyd]

#%%
# Writing to a text file - <outfile>.write(str(<obj>), <outfile>.writelines([str(<obj>)+'\n' for <obj> in <objs>])

# print(type(get_data_dir()))
# print(get_data_dir())
file = get_data_dir() / 'bands.txt'
with open(file, 'w') as f:
    # f.write(str(theRollingStones))
    f.writelines('\n'.join([str(b) for b in bands]))
print('Done.')

#%%
# Demonstrate reading from a text file - <infile>.read(), <infile>.readline(), <infile>.readlines()

file = get_data_dir() / 'bands.txt'
with open(file, 'r') as f:
    # b = f.readlines()                             # returns a list of lines
    # b = f.read()                                  # returns just lines, as one big string
    # print(b)
    lines = ''
    while True:
        line = f.readline()
        if line:
            lines += line
        else:
            break
print(lines)


#%%
# Demonstrate writing to a binary file - pickle.dump(<obj>, <outfile>)

file = get_data_dir() / 'bands'
with open(file, 'wb') as f:
    pickle.dump(bands, f)
print('Done.')

#%%
# Demonstrate reading from a binary file - pickle.load(<infile>)

file = get_data_dir() / 'bands'
with open(file, 'rb') as f:
    b = pickle.load(f)
# print(b)
for band in b:
    print(band)


