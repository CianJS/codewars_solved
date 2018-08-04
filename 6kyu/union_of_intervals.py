# -*- coding: utf-8 -*-

'''
Description:
 Union of closed disjoint intervals
 Write a function interval_insert which takes as input

 a list myl of disjoint closed intervals with integer endpoints, sorted by increasing order of left endpoints
 an interval interval
 and returns the union of interval with the intervals in myl, as an array of disjoint closed intervals.

Examples:
 [(1, 2)], (3, 4) -> [(1, 2), (3, 4)]
 [(3, 4)], (1, 2) -> [(1, 2), (3, 4)]
 [(1, 2), (4, 6)], (1, 4) -> [(1, 6)]
 [(0, 2), (3, 6), (7, 7), (9, 12)], (1, 8) -> [(0, 8), (9, 12)]
'''

def interval_insert (myl, interval):
    ans = []
    a = interval[0]
    b = interval[1]
    for x in myl:
        if x[1] < a or b < x[0]: # no intersection
            ans.append(x)
        else: # intersection
            a = min(x[0],a)
            b = max(x[1],b)
    ans.append((a,b))
    return sorted(ans)

# print interval_insert([(1,2)], (3,4)), [(1, 2), (3, 4)]
# print interval_insert([(135, 136), (140, 142)], (137, 139)), [(135, 136), (137, 139), (140, 142)]
# print interval_insert([(-85, -84), (-80, -78)], (-79, -78)), [(14, 17)]
# print interval_insert([(-85, -84), (-80, -78)], (-79, -78)), [(-85, -84), (-80, -78)]
# print interval_insert([(1, 2), (3, 4)], (2,3)), [(1, 4)]
