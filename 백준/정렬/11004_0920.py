# 백준 11004번 - 정렬 K번째수
import sys
n, k = map(int,input().split(' '))
num = list(map(int, sys.stdin.readline().split(' ')))

num.sort()

print(num[k-1])