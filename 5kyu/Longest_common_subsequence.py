# -*- coding: utf-8 -*-

'''
Example -
lcs( "abcdef", "abc" ) => returns "abc"
lcs( "abcdef", "acf" ) => returns "acf"
lcs( "132535365", "123456789" ) => returns "12356"
'''

def lcs(x, y):
    '''
    :param x: target string
    :param y: search string
    :return: exist string in x
    '''
    result = ''
    remove_str = set()

    split_x = set(','.join(x).split(','))
    for st_y in y:
        if st_y not in split_x:
            remove_str.add(st_y)

    for i in remove_str:
        y = y.replace(i, '')

    for st_y in y:
        for st_x in x:
            if st_y in st_x:
                result += st_y
                break

        x = x[1:]
    return result

if __name__ == "__main__":
    print lcs("abcdef", "abc") == "abc"
    print lcs("abcdef", "acf") == "acf"
    print lcs("132535365", "123456789") == "12356"
    print lcs("anothertest", "notatest") == "nottest"
    print lcs("finaltest", "zzzfinallyzzz") == "final"
