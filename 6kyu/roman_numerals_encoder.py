# -*- coding: utf-8 -*-

'''
python version: 2.7

Modern Roman numerals are written by expressing each digit separately starting with
the left most digit and skipping any digit with a value of zero.
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.
'''

def solution(n):
    # Roman numerals
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    # n의 각 자리의 값의 구분을 위해 list로 변환
    val = [i for i in str(n)]
    val.reverse()

    for i in range(0, len(val)):
        addZero = ''
        for idx in range(0, i):
            addZero += '0'
        val[i] = int(val[i] + addZero)

    result = ''
    val.reverse()

    for v in val:
        while(v != 0):
            if (str(v)[0] == '9') or str(v)[0] == '4':
                if I < v < V:
                    result += 'IV'
                elif V < v < X:
                    result += 'IX'
                elif X < v < L:
                    result += 'XL'
                elif L < v < C:
                    result += 'XC'
                elif C < v < D:
                    result += 'CD'
                elif D < v < M:
                    result += 'CM'
                v = 0

            if v >= M:
                for i in range(0, v / M):
                    result += 'M'
                    v -= M
            elif v >= D:
                for i in range(0, v / D):
                    result += 'D'
                    v -= D
            elif v >= C:
                for i in range(0, v / C):
                    result += 'C'
                    v -= C
            elif v >= L:
                for i in range(0, v / L):
                    result += 'L'
                    v -= L
            elif v >= X:
                for i in range(0, v / X):
                    result += 'X'
                    v -= X
            elif v >= V:
                for i in range(0, v / V):
                    result += 'V'
                    v -= V
            elif v >= I:
                for i in range(0, v / I):
                    result += 'I'
                    v -= I

    return result

if __name__ == "__main__":
    print(solution(1) == 'I')
    print(solution(2) == 'II')
    print(solution(3) == 'III')
    print(solution(4) == 'IV')
    print(solution(6) == 'VI')
    print(solution(14) == 'XIV')
    print(solution(21) == 'XXI')
    print(solution(89) == 'LXXXIX')
    print(solution(91) == 'XCI')
    print(solution(984) == 'CMLXXXIV')
    print(solution(1000) == 'M')
    print(solution(1889) == 'MDCCCLXXXIX')
    print(solution(1989) == 'MCMLXXXIX')