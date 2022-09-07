# 백준 10814번 _ 나이순 정렬

import sys

num = int(sys.stdin.readline())

res = []

for i in range(num):
  loc = 0
  s = list(sys.stdin.readline().strip().split(' '))
  
  for j in range(i):
    if int(s[0]) < int(res[j].split(' ')[0]):
      loc = j
      break
    else: loc = j+1

  res.insert(loc, s[0]+' '+s[1])

print(lambda x : x, res)