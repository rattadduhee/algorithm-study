# 백준 - 그리디 1783번 - 병든 나이트

n, m = map(int, input().split())
count = 0

if n == 1:
    count = 1
elif n == 2:
    count = min(4, (m-1)//2 + 1)
elif m < 7:
    count = min(4, m)
else:
    count = m - 2

print(count)