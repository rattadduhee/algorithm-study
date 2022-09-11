from re import L
import sys

num = int(sys.stdin.readline())

for i in range(1, num+1):
  j = num - i
  s = ' ' * j
  if i == num:
    s += '*' * (i*2-1)
  else:
    s += '*'
    k = i * 2 - 3
    if k > 0:
      s += ' ' * k
      s += '*'
  print(s)

