from re import L
import sys

num = int(sys.stdin.readline())

for i in range(1, num+1):
  j = num - i
  s = ' ' * j
  for i2 in range(1, i+1):
    k = i2-1
    if k > 0:
      s += ' '
      k -= 1
    s += '*'
  print(s)

