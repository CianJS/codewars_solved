# -*- coding: utf-8 -*-

# TODO: Replace examples and use TDD development by writing your own tests
# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

# You can use Test.describe and Test.it to write BDD style test groupings

class Calculator(object):
    def evaluate(self, string):
        calc_lt = string.split(' ')
        result = ''
        for val in calc_lt:
            try:
                if val in ('()+-*/') or float(val):
                    result += val
            except ValueError:
                return False
        return round(eval(result),4)

if __name__ == "__main__":
    test1 = "Hello + TDD * WORLD"
    test2 = "( 3 + 4 ) * 3 / ( 7 - 6 )"
    test3 = "3 + 4 * 5 / 2 - 7"
    test4 = "10 * 5 / 2"
    test5 = "1.1 + 2.2 + 3.3"
    test6 = "1.1 * 2.2 * 3.3"

    test_str = Calculator
    test_str().evaluate(test1)
    test_str().evaluate(test2)
    result = test_str().evaluate(test3)
    result2 = test_str().evaluate(test4)
    print result == 6, result2 == 25