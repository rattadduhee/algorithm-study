# 백준 9613번 - 기초수학 - GCD 합
# ★★★ combinations 함수 활용

import sys
from itertools import combinations

t = int(input())

for _ in range(t):
  num = list(map(int, sys.stdin.readline().split(' ')))
  n = num[0]
  num = num[1:]
  res = 0
  num = list(combinations(num, 2))
  
  for i in num:
    if i[1]>i[0]:
      a, b = i[1], i[0]
    else: 
      a, b = i[0], i[1]
    while b:
      a, b = b, a%b 
    res += a
  print(res)


