# 백준- 문자열처리 11655번 - ROT13

s = input()
res = ''
cap_al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
min_al = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'

for i in range(len(s)):
    if s[i] in num or s[i] == ' ':
        res += s[i]
    if s[i] in cap_al:
        temp = int(ord(s[i])) + 13
        if temp > ord('Z'):
            res += chr(temp - 26)
        else:
            res += chr(temp)
    if s[i] in min_al:
        temp = int(ord(s[i])) + 13
        if temp > ord('z'):
            res += chr(temp - 26)
        else:
            res += chr(temp)


print(res)