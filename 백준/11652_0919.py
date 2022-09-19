# 백준 11652번 - 정렬 - 카드

import sys
from collections import Counter

n = int(sys.stdin.readline())
s = [] 

for _ in range(n):
  s.append(int(input()))

s = Counter(s).most_common()
temp = 0
for i in s:
  if temp < i[1]:
    res = []
    temp = i[1]
    res.append(i[0])
  elif temp == i[1]:
    res.append(i[0])

print(min(res))