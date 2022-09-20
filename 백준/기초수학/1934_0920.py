# 백준 2609번 - 기초수학 - 최소공배수

def f(a,b):
  while b :
    a, b = b, a%b
  return a

import sys

n = int(input())
for _ in range(n):
  a, b = map(int, sys.stdin.readline().split(' '))
  print((a*b)//f(a,b))