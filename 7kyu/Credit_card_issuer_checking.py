# -*- coding: utf-8 -*-

'''
| Card Type  | Begins With          | Number Length |
|------------|----------------------|---------------|
| AMEX       | 34 or 37             | 15            |
| Discover   | 6011                 | 16            |
| Mastercard | 51, 52, 53, 54 or 55 | 16            |
| VISA       | 4                    | 13 or 16      |

Write the function at looking the table above.
'''

import sys
from .tester import credit_card_issuer_checking_test as test

sys.path.append("C:/Python/Mymodules")

def getIssuer(number):
    number = str(number)
    if len(number) == 15:
        if number[:2] in ('34','37'):
            return 'AMEX'
        else:
            return 'Unknown'
    elif len(number) == 16:
        if int(number[:2]) in range(51,56):
            return 'Mastercard'
        elif number[0] == '4':
            return 'VISA'
        elif number[:4] == '6011':
            return 'Discover'
        else:
            return 'Unknown'
    elif len(number) == 13:
        if number[0] == '4':
            return 'VISA'
        else:
            return 'Unknown'
    else:
        return 'Unknown'

if __name__ == "__main__":
    test.assert_equals(getIssuer(4111111111111111), 'VISA')
    test.assert_equals(getIssuer(378282246310005), 'AMEX')
    test.assert_equals(getIssuer(9111111111111111), 'Unknown')