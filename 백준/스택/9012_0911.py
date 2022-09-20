# 백준 9012번 - 괄호

num = int(input())

for _ in range(num):
    res = []
    cnt = 0
    s = input().strip()
    for i in range(len(s)):
        if s[i] == '(':
            res.append('(')
        if s[i] == ')':
            if len(res) > 0:
                res.pop()
            else:
                cnt += 1
                break

    if len(res) > 0 or cnt > 0:
        print('NO')
    else:
        print('YES')
