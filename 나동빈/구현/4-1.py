# 구현 - 상하좌우

import sys

num = int(input())
s = list(sys.stdin.readline().strip().split(' '))
x = 1
y = 1
print(s)

for i in s:
    if (i == 'L') and (y > 1):
        y -= 1
    if (i == 'R') and (y < num):
        y += 1
    if (i == 'U') and (x > 1):
        x -= 1
    if (i == 'D') and (x < num):
        x += 1

print(x, y)