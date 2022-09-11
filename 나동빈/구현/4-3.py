# 구현 - 왕실의 나이트

import sys

# steps = [(2,1), (2,-1), ..., (-1,2), (-1,-2)]   : 하나의 리스트로 표현가능
dx = [+2, +2, -2, -2, +1, +1, -1, -1]
dy = [+1, -1, +1, -1, +2, -2, +2, -2]

# x = int(ord(s[0])) - int(ord('a')) + 1    : 아스키 코드를 이용한 변환 (ord함수 이용)
x_num = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

result = 0

s = input()

x = int(x_num[s[0]])
y = int(s[1])

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 < nx < 9 and 0 < ny < 9:
        result += 1

print(result)
