# 백준 11576번 - 기초수학 - Base Conversion

from re import S


a, b = map(int, input().split())
m = int(input())
num = list(map(int,input().split()))
result = []
n = 0
num.reverse()

for i in range(m):
  n += num[i]*(a**i)

while n//b:
  result.append(n%b)
  n //= b
result.append(n)
result.reverse()
print(' '.join(map(str,result)))
