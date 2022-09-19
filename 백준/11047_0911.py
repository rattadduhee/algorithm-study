# 백준 - 그리디 11047번 - 동전 0

n, k = map(int, input().split())
dong = []
count = 0

for _ in range(n):
    dong.append(int(input()))

dong.sort(reverse = True)

for i in dong:
    if k >= i:
        count += k // i
        k = k % i 
    
    if k == 0:
        break

print(count)