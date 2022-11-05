# 백준 1978번 - 기초수학 - 소수찾기

n = int(input())
num = list(map(int, input().split()))
res = 0

for i in num:
  tp = 0
  if i == 1:
    continue
  for j in range(int(i)-1, 1, -1):
      if i % j == 0:
        tp += 1
  if tp == 0:
    res += 1

print(res)