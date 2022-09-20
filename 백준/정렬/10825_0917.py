# 백준 10825 - 국영수
import sys

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    s.append(list(sys.stdin.readline().strip().split(' ')))

s = sorted(s, key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in s:
    print(i[0])
