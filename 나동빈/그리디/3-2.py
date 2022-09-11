# 그리디 - 큰 수의 법칙

import sys

n, m, k = map(int, sys.stdin.readline().split(' '))
num = list(map(int, sys.stdin.readline().split(' ')))
result = 0

num.sort()
n1 = num[-1]
n2 = num[-2]

while m > 0:
    for _ in range(k):
        result += n1
        m -= 1
    
    result += n2
    m -= 1

print(result)

# 가장 큰 수 가 더해지는 횟수
# count = int(m / (k+1)) *k
# count += m%(k+1)
