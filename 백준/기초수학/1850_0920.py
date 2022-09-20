# 백준 1850번 - 기초수학 - 최대공약수

import sys
a, b = map(int, sys.stdin.readline().split(' '))

if b > a:
  a,b = b,a
while b:
  a, b = b, a%b

print('1'*a)
