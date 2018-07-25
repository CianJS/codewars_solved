# -*- coding: utf-8 -*-

'''
https://www.codewars.com/kata/inverting-a-hash/ 참조
'''

def invert_hash(dictionary):
    result = {}
    for key, value in dictionary.copy().iteritems():
        result[value] = key
    return result

if __name__ == "__main__":
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    invert_hash(test_dict)