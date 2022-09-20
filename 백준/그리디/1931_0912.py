# 백준 1931번 - 그리디 - 회의실배정

n = int(input())
h = []
count = 0

for i in range(n):
    h.append(list(map(int, input().split())))

h.sort(key = lambda x : (x[1], x[0]))

res = []

for i in h:
    if len(res) == 0:
        res.append(i[1])
    else:
        if res[-1] <= i[0]:
            res.append(i[1])

print(len(res))