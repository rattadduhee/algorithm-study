# 백준 2609번 - 기초수학 - 최대공약수와 최소공배수

def f1(a, b):
  while b:
    a, b = b, a%b
  return a

def f2(a,b):
  return ((a*b) // f1(a,b))
  
import sys
a,b = map(int, sys.stdin.readline().split(' '))

print(f1(a,b))
print(f2(a,b))