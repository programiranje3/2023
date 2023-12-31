"""Demonstrates details of writing Python functions: annotations, default args, kwargs.
"""


#%%
# Setup / Data
song = 'Honky Tonk Woman'
year = 1969

mick = 'Mick Jagger'
keith = 'Keith Richards'
charlie = 'Charlie Watts'
brian = 'Brian Jones'
bill = 'Bill Wyman'
the_rolling_stones = [mick, keith, charlie, brian, bill]


#%%
def demonstrate_annotations(title, year):
    """Demonstrates how to use annotations of
    function parameters/arguments (<arg>: <type>) and of function return type (def f(...) -> <type>:).
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the name and the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """


#%%
# Test demonstrate_annotations(title, year)
print(demonstrate_annotations(song, year))


#%%
# def show_song(title, authors='Jagger/Richards', year: int = 1969):
def show_song(title, authors='Jagger/Richards', year=1969):

    """Demonstrates default arguments/parameters.
    - print locals()
    - print the function arguments/parameters in one line
    """


#%%
# Test show_song(title, authors='Jagger/Richards', year=1969)
show_song(song)


#%%
def use_flexible_arg_list(band: str, *members):
    """Demonstrates flexible number of arguments/parameters.
    - print the band name and the list of band members in one line
    """


#%%
# Test use_flexible_arg_list(band: str, *members)
use_flexible_arg_list('The Rolling Stones', *the_rolling_stones)
use_flexible_arg_list('The Rolling Stones')


#%%
def use_all_categories_of_args(band, *members, is_active=True, **details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """


#%%
# Test use_all_categories_of_args(band, *members, is_active=True, **details)
use_all_categories_of_args('The Rolling Stones', is_active=True, start=1962, end=2023)
use_all_categories_of_args('The Rolling Stones', *the_rolling_stones, is_active=False,
                           start=1962, end=2023)


