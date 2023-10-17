"""Demonstrates peculiarities of if, for, while and other statements.
"""


#%%
def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings and numbers, but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    # l1 = [26, 18]
    # l2 = [26, 18]
    #
    # print(l1 == l2)
    # print(l1 is l2)
    # print()
    #
    # a = 'Mick'
    # b = 'Mick'
    # print(a is b)

    # if 0.0:
    #     print(True)
    # else:
    #     print(False)

    n = 3
    if n == 3:
        print('3')
    elif n == 2:
        print('2')
    elif n ==1:
        print('1')
    else:
        print(0)


#%%
# Test demonstrate_branching()
demonstrate_branching()

#%%


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    # l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    # for e in l1:
    #     print(e, ', ', end='')
    # print()
    # for e in l1[3:-2]:
    #     print(e, ', ', end='')
    # print()
    # for e in l1[:-2]:
    #     print(e, ', ', end='')
    # print()

    s = 'Keith'
    # for i in range(len(s)):
    #     print(s[i], end='')
    # print()
    # for i in range(1, len(s), 2):
    #     print(s[i], end='')
    # print()
    for _ in range(len(s)):
        print('Mick and Keith')
    print()


#%%
# Test demonstrate_loops()
demonstrate_loops()
