# 백준 - 그리디 10610번 - 30

num = input()
count = 0

while True:
    if '0' not in num:
        print(-1)
        break

    res = int(num)

    if res % 30 == 0:
        print(res)
        break

