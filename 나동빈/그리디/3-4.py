# 그리디 - 1이 될 때까지

import sys

n, k = map(int, sys.stdin.readline().split(' '))
result = 0

while n > 1:
    if n % k == 0:
        n //= k
        result += 1
    else:
        n -= 1
        result += 1

print(result)