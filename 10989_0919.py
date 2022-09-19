# 백준 10989번 - 정렬 - 수정렬하기 3
# 메모리 초과 - 카운팅 정렬 & pypy대신 python 활용

from operator import iconcat
import sys

n = int(sys.stdin.readline())
count = [0] * 10000

for _ in range(n):
  count[int(sys.stdin.readline())] += 1

for i in range(1,len(count)):
  for _ in range(count[i]):
    print(i)