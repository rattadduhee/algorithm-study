# 백준 10814번 _ 나이순 정렬

import sys

num = int(sys.stdin.readline())

res = []

for i in range(num):
  res.append(sys.stdin.readline().strip())   # '\n'제거

# 숫자로만 값 정렬
res = sorted(res, key=lambda x : int(x.split()[0]))

for i in res:
  print(i)
