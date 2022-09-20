# 백준 1476번 - 완전탐색 - 날짜계산

e, s, m = map(int,input().split())
result = 0
k = 0

while True:
    result = s + 28 * k
    if (result - e) % 15 == 0 and (result - m) % 19 == 0:
        break
    k+=1

print(result)