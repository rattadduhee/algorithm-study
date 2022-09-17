# 백준 - 스택 - 10799번

s = input()
cut_n = 0
bar_n = 0
result = 0
temp = []

for i in range(len(s)-2,-1,-1):
    if s[i:i+2] == '))':
        bar_n += 1
        temp.append(i)
    if s[i:i+2] == '()':
        result += bar_n
    if s[i:i+2] == '((':
        if len(temp) != 0:
            temp.pop()
            bar_n -= 1
            result += 1
 
print(result)
