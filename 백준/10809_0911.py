# 백준- 문자열처리 10809번 - 알파벳 찾기

s = input().strip()
al = [-1] * 26

for i in range(len(s)):
    if al[int(ord(s[i])) - int(ord('a'))] == -1:
        al[int(ord(s[i])) - int(ord('a'))] = i

for i in al:
    print(i, end=' ')