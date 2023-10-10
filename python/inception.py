"""The very first module in a more structured version of the project.
"""


#%%
# # Moving code from main.py
#
# # Hello world: the print() built-in function and the + operator.
#
# print('Mick Jagger')
# print('Mick Jagger', 'was born in', 1943)
# print('Mick Jagger', 'was born in ' + str(1943))

#%%
# Printing with ' ' and printing without '\n'

print('Keith Richards', 'was born in:', '\n' + str(1943))
print('The Rolling Stones released the single \'Angry\' in 2023.')

#%%
# Printing with classical formatting (%)

print('Keith Richards was born in %s, in %d' % ('Dartford, UK', 1943))

#%%
# Keyboard input


#%%
# break and continue

for i in range(5):
    if i == 3:
        # continue
        break
    print(i)

#%%
# A simple function and function call


def year_of_birth():
    """
    year_of_birth
    :return: year
    """
    print('Keith Richards was born in: ', end='')
    year = input()
    return year


print(year_of_birth())

#%%
# Printing docstrings

print(year_of_birth.__doc__)

#%%
# Printing a list using enumerate()


#%%
# Importing from Standard Library

# Date format strings
# https://docs.python.org/3/library/datetime.html?highlight=date%20format%20strings#strftime-and-strptime-format-codes

from datetime import date

birthday_mick = date(1943, 7, 26)
birthday_keith = date(1943, 12,18)

print(birthday_keith)

date_format = '%b %d, %Y'
print(birthday_mick.strftime(date_format))

#%%
# Testing print(__file__)

print(__name__)

#%%
# Taking care of the module __name__

if __name__ == '__main__':
    print('Mick Jagger')
    print('Mick Jagger', 'was born in', 1943)
    print('Mick Jagger', 'was born in ' + str(1943))


