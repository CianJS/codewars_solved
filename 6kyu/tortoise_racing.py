# -*- coding: utf-8 -*-

'''
Description:
 Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour. Young B knows she runs faster than A and furthermore has not finished her cabbage.
 When she starts, at last, she can see that A has a 70 feet lead but B speed is 850 feet per hour. How long will it take B to catch A?
 More generally: given two speeds v1 (A speed, integer > 0) and v2 (B speed, integer > 0) and a lead g (integer > 0) how long will it take B to catch A?
 The result will be an array [h, mn, s] where h, mn, s is the time needed in hours, minutes and seconds (don't worry for fractions of second). If v1 >= v2 then return nil, nothing, null, None or {-1, -1, -1} for C++.

Examples:
 race(720, 850, 70) => [0, 32, 18]
 race(80, 91, 37) => [3, 21, 49]
'''

def race(v1, v2, g):
    if (v1 <= 0 and v2 <= 0 and g <= 0) or v1 >= v2:
        return None
    result = 3600 * g / (v2 - v1)
    return [int(result / 60 / 60), int(result / 60 % 60), int(result % 60)]

print race(720, 850, 70), [0, 32, 18]
print race(80, 91, 37), [3, 21, 49]
print race(80, 100, 40), [2, 0, 0]
