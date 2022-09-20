# 백준 - 그리디 11399번 - ATM

n = int(input())
p = list(map(int, input().split()))
count = 0
result = 0

p.sort()

for i in range(len(p)):
    count += p[i]
    p[i] = count
    result += count

print(result)
