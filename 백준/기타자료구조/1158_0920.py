# 백준 1158번 - 기타자료구조 - 요시푸스 문제

import sys

n, k = map(int, input().split(' '))
s = list(range(1,n+1))
res = []
i = 0

while len(s) != 0:
  i += k-1
  while i >= len(s):
    i -= len(s)
  res.append(str(s.pop(i)))
  
print('<', ', '.join(res),'>', sep='')
