# 백준 1463번 풀이

import sys

x = int(sys.stdin.readline())

# DP 배열 생성
res = [0] * (x+1)

for i in range(2, x+1):
    res[i] = res[i-1] + 1    
    if i % 3 == 0 :
        res[i] = min(res[i], res[i//3] + 1)
    if i % 2 == 0 :
        res[i] = min(res[i], res[i//2] + 1)

print(res.pop())