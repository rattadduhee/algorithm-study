# 백준- 문자열처리 10820번 - 문자열 분석

import sys

cap_al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
min_al = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'

while True:
    res = [0, 0, 0, 0]
    s = sys.stdin.readline()
    if not s: break

    for i in range(len(s)):
        if s[i] in min_al:
            res[0] += 1   
        if s[i] in cap_al:
            res[1] += 1 
        if s[i] in num:
            res[2] += 1
        if s[i] == ' ':
            res[3] += 1

    for i in res:
        print(i, end=' ')
    