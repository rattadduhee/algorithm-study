# 백준 10430번 - 기초수학 - 나머지

import sys

a, b, c = map(int, sys.stdin.readline().split(' '))

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)