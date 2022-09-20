# 백준 2745번 - 기초수학 - 진법변환

import sys

n, b = input().split(' ')
b = int(b)
res = 0
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
temp = 1
n = n[::-1]
for i in range(len(n)):
  if n[i] in s:
    for j in range(len(s)):
      if n[i] == s[j]:
        res += (j+10) * temp
  else:
    res += n[i] * temp
  temp *= b

print(res)