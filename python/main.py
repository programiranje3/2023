# """The very first Python script - main.py.
# """
#
#
# #%%
# # Hello world: the print() built-in function and the + operator.
#
# print('Mick Jagger')
# print('Mick Jagger', 'was born in', 1943)
# print('Mick Jagger', 'was born in ' + str(1943))
#
# #%%
# # The input() built-in function
#
# # print('Keith Richards was born in: ', end='')
# # year = input()
# # print('Keith Richards was born in', year)
#
# print('Keith Richards was born in', int(input()))
#
# #%%
# # A simple function and function call
#
#
# def year_of_birth():
#     """
#     year_of_birth
#     :return: year
#     """
#     print('Keith Richards was born in: ', end='')
#     year = input()
#     return year
#
#
# print(year_of_birth())
#
# #%%
# # A simple loop and the range() built-in function
#
# # for i in range(5):
# #     print(i)
#
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#
# #%%
# # A simple list, accessing list elements, printing lists
#
# songs = ['A girl with faraway eyes', 'Angry', 'Waiting on a friend']
#
# print(songs[0])
# print(songs)
# print(type(songs[1]))
# print(type(songs))
#
# #%%
# # Looping through list elements - for and enumerate()
#
# songs = ['A girl with faraway eyes', 'Angry', 'Waiting on a friend']
#
# # for s in songs:
# #     print(s)
#
# # print(enumerate(songs))
# # print(list(enumerate(songs, start=1)))
# # for i, s in enumerate(songs):
# #     print(str(i) + ':', s)
# for i, s in enumerate(songs, start=1):
#     print(str(i) + ':', s)
#
# #%%
# # Global variables: __name__, __file__, __doc__,...
#
# print(__name__)
# # print(__file__)
# print(__doc__)
# print(year_of_birth.__doc__)

#%%
# Importing from another script

from inception import year_of_birth
print(year_of_birth())

