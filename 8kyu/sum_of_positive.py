# -*- coding: utf-8 -*-

'''
You get an array of numbers, return the result of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to result, the result is default to 0.
'''

def positive_result(arr):
    result = 0
    for i in arr:
        if i > 0:
            result += i
    return result

if __name__ == "__main__":
    print(positive_result([1, 2, 3, 4, 5]), 15)
    print(positive_result([1, -2, 3, 4, 5]) == 13)
    print(positive_result([-1, 2, 3, 4, -5]) == 9)