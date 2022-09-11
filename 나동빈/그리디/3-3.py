# 그리디 - 숫자 카드 게임

import sys

n,m = map(int, sys.stdin.readline().split(' '))
result = 0

for _ in range(n):
    num = map(int, sys.stdin.readline().split(' '))
    min_num = min(num)

    result = max(result, min_num)

print(result)