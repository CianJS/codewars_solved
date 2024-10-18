/**
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1
Help
+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+
 */

const romanToIntegerMap = {
  M: 1000,
  CM: 900,
  D: 500,
  CD: 400,
  C: 100,
  XC: 90,
  L: 50,
  XL: 40,
  X: 10,
  IX: 9,
  V: 5,
  IV: 4,
  I: 1,
};
const valueToRomanSymbolMap = {
  1000: 'M',
  900: 'CM',
  500: 'D',
  400: 'CD',
  100: 'C',
  90: 'XC',
  50: 'L',
  40: 'XL',
  10: 'X',
  9: 'IX',
  5: 'V',
  4: 'IV',
  1: 'I',
};

class RomanNumerals {
  static toRoman(num) {
    let temp = num;
    let result = '';
    const values = Object.keys(valueToRomanSymbolMap)
      .sort((a, b) => b - a)
      .map(Number);
    while (temp > 0) {
      values.some((v) => {
        if (temp >= v) {
          temp -= v;
          result += valueToRomanSymbolMap[v];
          if (temp >= v || temp <= 0) return true;
        }
      });
    }
    return result;
  }

  static fromRoman(str) {
    let result = 0;
    const splittedStr = str.split('');
    splittedStr.reduce((a, c, i) => {
      if (!romanToIntegerMap[c]) return a;
      if (romanToIntegerMap[c + splittedStr[i + 1]]) return c;
      if (a) result += romanToIntegerMap[a + c];
      else result += romanToIntegerMap[c];
      return '';
    }, '');
    return result;
  }
}

function isEqual(testFunction, romanji) {
  console.log(testFunction == romanji);
  return testFunction == romanji;
}

// to
isEqual(RomanNumerals.toRoman(1000), 'M');
isEqual(RomanNumerals.toRoman(4), 'IV');
isEqual(RomanNumerals.toRoman(1), 'I');
isEqual(RomanNumerals.toRoman(1990), 'MCMXC');
isEqual(RomanNumerals.toRoman(2008), 'MMVIII');

// from
isEqual(RomanNumerals.fromRoman('XXI'), 21);
isEqual(RomanNumerals.fromRoman('I'), 1);
isEqual(RomanNumerals.fromRoman('IV'), 4);
isEqual(RomanNumerals.fromRoman('MMVIII'), 2008);
isEqual(RomanNumerals.fromRoman('MDCLXVI'), 1666);
