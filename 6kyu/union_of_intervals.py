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

def interval_insert(myl, interval):
    result = []
    l = interval[0]
    r = interval[1]
    l_tmp = []
    r_tmp = []
    idx = -1

    for begin, end in sorted(myl):
        idx += 1
        if not l_tmp:
            if l >= begin:
                # l_tmp exist by end value
                if l == begin:
                    l_tmp.append(l)
                    if r <= end:
                        r_tmp.append(end)
                elif l == end:
                    l_tmp.append(begin)
                elif l > end:
                    result.append((begin, end))
                    if len(myl) == 1:
                        result.append(interval)
                    elif len(myl) == idx + 1:
                        result.append(interval)
                elif l < end:
                    if r < end:
                        result.append((l, end))
                    elif r == end:
                        result.append((begin, end))
                    elif r > end:
                        result.append((begin, r))
                    else:
                        l_tmp.append(begin)
            else:
                l_tmp.append(l)
                if r < begin:
                    r_tmp.append(r)
                    result.append((begin, end))
                elif r <= end:
                    r_tmp.append(end)
        elif not r_tmp:
            if r < begin:
                r_tmp.append(r)
                result.append((begin, end))
            elif r == begin:
                r_tmp.append(end)
            elif r > begin:
                if r > end:
                    if len(myl) == idx +1:
                        r_tmp.append(r)
                    continue
                elif r == end:
                    r_tmp.append(r)
                elif r < end:
                    r_tmp.append(end)
        else:
            result.append((begin, end))

    if len(l_tmp + r_tmp) == 2:
        result.append(tuple(l_tmp + r_tmp))

    return sorted(result)

# print interval_insert([(1,2)], (3,4)), [(1, 2), (3, 4)]
# print interval_insert([(135, 136), (140, 142)], (137, 139)), [(135, 136), (137, 139), (140, 142)]
# print interval_insert([(-85, -84), (-80, -78)], (-79, -78)), [(14, 17)]
# print interval_insert([(-85, -84), (-80, -78)], (-79, -78)), [(-85, -84), (-80, -78)]
# print interval_insert([(1, 2), (3, 4)], (2,3)), [(1, 4)]
# print interval_insert([(1, 2), (3, 4), (5, 6)], (2, 3)), [(1, 4), (5, 6)]
# print interval_insert([(0, 2), (3, 6), (7, 7), (9, 12)], (1, 8)), [(0, 8), (9, 12)]
# print interval_insert([(114, 116), (119, 120), (124, 127), (129, 130), (134, 136), (139, 141), (144, 145), (149, 152)], (151, 156)) == [(114, 116), (119, 120), (124, 127), (129, 130), (134, 136), (139, 141), (144, 145), (149, 156)]
# print interval_insert([(-63, -60), (-58, -56), (-53, -51), (-48, -47), (-43, -42), (-38, -37), (-33, -30), (-28, -27)], (-43, -20)), [(-63, -60), (-58, -56), (-53, -51), (-48, -47), (-43, -20)]
# print interval_insert([(18, 21), (23, 25), (28, 31), (33, 36), (38, 39)], (17, 39)), [(17, 39)]
# print interval_insert([(114, 116), (124, 125), (134, 137), (144, 147), (154, 157), (164, 165)], (171, 174)), [(114, 116), (124, 125), (134, 137), (144, 147), (154, 157), (164, 165), (171, 174)]
# print interval_insert([(-90, -88), (-85, -82), (-80, -78), (-75, -74), (-70, -68), (-65, -64), (-60, -58), (-55, -52), (-50, -48)], (-80, -50)), [(-90, -88), (-85, -82), (-80, -48)]
