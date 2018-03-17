# -*- coding: utf-8 -*-

import os
import sys
import unittest
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Calculator import Calculator as Calc

class Calculator_spec(unittest.TestCase):
    def __init__(self):
        self.Calcs = Calc()

    def test_string_expect(self):
        self.assertFalse(self.Calcs.evaluate("Hello TDD WORLD"))
        self.assertFalse(self.Calcs.evaluate("Hello + TDD * WORLD"))
        self.assertTrue(self.Calcs.evaluate("3 + 4 * 5 / 2 - 7"))

    def test_assert_equals(self):
        self.assertEqual(self.Calcs.evaluate("3 + 4 * 5 / 2 - 7"), 6, "Success")
        self.assertEqual(self.Calcs.evaluate("10 * 5 / 2"), 25, "Success")
        self.assertEquals(self.Calcs.evaluate("1.1 + 2.2 + 3.3"), 6.6, "Success")
        self.assertEquals(self.Calcs.evaluate("1.1 * 2.2 * 3.3"), 7.986, "Success")

    def test_assert_not_equals(self):
        self.assertNotEquals(self.Calcs.evaluate("( 3 + 4 ) * 3 / ( 7 - 6 )"), -4)

    def assertEquals_test(self, key, result, msg):
        self.assertEqual(key, result, msg)

if __name__ == '__main__':
    test_case = Calculator_spec
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
    # test = Calculator_spec()
    # for key, val in {
    #     "127": 127,
    #     "2 + 3": 5,
    #     "2 - 3 - 4": -5,
    #     "10 * 5 / 2": 25,
    #     "2 / 2 + 3 * 4 - 6": 7,
    #     "2 + 3 * 4 / 3 - 6 / 3 * 3 + 8": 8,
    #     "1.1 + 2.2 + 3.3": 6.6,
    #     "1.1 * 2.2 * 3.3": 7.986
    # }.items():
    #     actual = self.Calcs(key)
    #     suite = unittest.TestLoader().loadTestsFromModule(test)
    #     unittest.TextTestRunner().run(suite)
    #     test.assertEquals_test(actual, val, "Expected %s == %s, got %s" % (key, str(val), str(actual)))