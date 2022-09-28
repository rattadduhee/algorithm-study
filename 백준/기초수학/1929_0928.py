# 백준 1929번 - 기초수학 - 소수구하기
import math
import sys
m, n = map(int, sys.stdin.readline().split())
res = []


for i in range(m, n+1):
  tp = 0
  for j in range(2, int(math.sqrt(i)+1)):
    if i%j == 0:
      tp+=1
      break

  if tp == 0:
    res.append(i)

print('\n'.join(map(str,res)))
