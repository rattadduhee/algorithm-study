# 백준 - 이분/삼분탐색 1654번 - 수 묶기

k, n = map(int, input().split())
lan = []
result = 0

for _ in range(k):
    lan.append(int(input()))

start = 1
end = max(lan)

while start <= end:
    num = 0
    mid = (start + end) // 2

    for i in lan:
        num += i // mid

    if num < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)