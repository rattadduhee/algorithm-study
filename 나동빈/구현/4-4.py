# 구현 - 게임개발

from ast import NotIn
import sys

row, col = map(int, sys.stdin.readline().split(' '))
x, y, di = map(int, sys.stdin.readline().split(' '))
game_map = []
move = [[-1,0], [0,1], [1,0], [0,-1]]
result = []
count = 0

for _ in range(row):
    game_map.append(list(map(int,sys.stdin.readline().split(' '))))

result.append([x,y])

while True :
    if game_map[x + move[di][0]][y + move[di][1]] != 1:
        if [x + move[di][0], y + move[di][1]] in result:
            di -= 1
            count += 1
            if di < 0: di = 3
        else :
            x += move[di][0]
            y += move[di][1]
            result.append([x,y])
            di -= 1
            count += 1
            if di < 0: di = 3

        if count > 3 :
            if game_map[x + move[di-2][0]][y + move[di-2][1]] != 1:
                x += move[di-2][0]
                y += move[di-2][1]
                count = 0
            else: break
    else :
        di -= 1
        count += 1
        if di < 0: di = 3

        if count > 3 :
            if game_map[x + move[di-2][0]][y + move[di-2][1]] != 1:
                x += move[di-2][0]
                y += move[di-2][1]
                count = 0
            else: break

print(result)
print(len(result))
