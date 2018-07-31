# -*- coding: utf-8 -*-

import unittest
import Calculator as Calc

class Calculator_spec(unittest.TestCase):
    Calcs = Calc.Calculator()

    def test_string_expect(self):
        self.assertFalse(Calculator_spec.Calcs.evaluate("Hello TDD WORLD"))
        self.assertFalse(Calculator_spec.Calcs.evaluate("Hello + TDD * WORLD"))
        self.assertTrue(Calculator_spec.Calcs.evaluate("3 + 4 * 5 / 2 - 7"))

    def test_assert_equals(self):
        Calcs = Calc.Calculator()
        self.assertEqual(Calcs.evaluate("3 + 4 * 5 / 2 - 7"), 6, "Success")
        self.assertEqual(Calcs.evaluate("10 * 5 / 2"), 25, "Success")
        self.assertEquals(Calcs.evaluate("1.1 + 2.2 + 3.3"), 6.6, "Success")
        self.assertEquals(Calcs.evaluate("1.1 * 2.2 * 3.3"), 7.986, "Success")

    def test_assert_not_equals(self):
        Calcs = Calc.Calculator()
        self.assertNotEquals(Calcs.evaluate("( 3 + 4 ) * 3 / ( 7 - 6 )"), -4)

    def assertEquals_test(self, key, result, msg):
        self.assertEqual(key, result, msg)

if __name__ == '__main__':
    test_case = Calculator_spec()
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
    #     actual = test.Calcs
    #     suite = unittest.TestLoader().loadTestsFromModule(test)
    #     unittest.TextTestRunner().run(suite)
    #     test.assertEquals_test(actual, val, "Expected %s == %s, got %s" % (key, str(val), str(actual)))