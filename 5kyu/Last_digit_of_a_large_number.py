# -*- coding: utf-8 -*-

'''
Example -

llast_digit(4, 1)                # returns 4
llast_digit(4, 2)                # returns 6
llast_digit(9, 7)                # returns 9
llast_digit(10, 10 ** 10)        # returns 0
llast_digit(2 ** 200, 2 ** 300)  # returns 6
'''

def last_digit(n1, n2):
    n1 = int(str(n1)[-1:])
    n2 = int(str(n2)[-2:])

    if n1 == 0 or str(n2)[-1:] == 0:
        n = 0
    else:
        n = n1 ** n2
    return int(str(n)[-1:])


if __name__ == "__main__":
    print("Example tests")
    print(last_digit(1, 0) == 1)
    print(last_digit(4, 1) == 4)
    print(last_digit(4, 2) == 6)
    print(last_digit(9, 7) == 9)
    print(last_digit(10, 10 ** 10) == 0)
    print(last_digit(2 ** 200, 2 ** 300) == 6)
    print(last_digit(3715290469715693021198967285016729344580685479654510946723,
                                  68819615221552997273737174557165657483427362207517952651) == 7)

    for nmbr in range(1, 9):
        a = nmbr ** nmbr
        print("Testing %d and %d" % (a, 0))
        print(last_digit(a, 0), 1, "x ** 0 must return 1")
