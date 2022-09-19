# 구현 - 시각

import sys

h = int(input())
result = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            s = str(i)+str(j)+str(k)
            if str(h) in s:
                result += 1

print(result)