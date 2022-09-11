# 구현 - 문자열 재정렬

s = input()
res = []
count = 0
s1 = ''
for i in s:
    # if i.isalpha():
    if int(ord(i)) >= 97:
        res.append(i)
    else:
        count += int(i)

res.sort() 

if count != 0:
    res.append(str(count))

print(''.join(res))