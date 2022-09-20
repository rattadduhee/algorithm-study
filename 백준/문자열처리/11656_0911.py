# 백준- 문자열처리 10656번 - 접미사 배열

s = input()
res = []

for i in range(len(s)):
    res.append(s[i:])

res.sort()

for i in res:
    print(i)