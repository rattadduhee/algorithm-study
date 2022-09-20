# 백준 11005번 - 기초수학 - 진법변환2

import sys

n, b = map(int,input().split(' '))
res = ''
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while n>0:
  n, mod = divmod(n,b)
  if mod > 9:
    res += s[mod-10]
  else:
    res += str(mod)

print(res[::-1])