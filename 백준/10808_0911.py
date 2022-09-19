# 백준- 문자열처리 10808번 - 알파벳 개수

s = input().strip()
al = [0] * 26

for i in range(len(s)):
    al[int(ord(s[i])) - int(ord('a'))] += 1

for i in al:
    print(i, end=' ')