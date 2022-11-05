# 프로그래머스 lv2 - 짝지어제거하기

def solution(s):
    answer = -1
    count = 0
    temp = []
    s = list(s)
    while s:
        t = s.pop()
        if len(temp)!=0:
            if t == temp[-1]:
                temp.pop()
            else:
                temp.append(t)
        else: 
            temp.append(t)
        
    answer = 1 if len(temp)==0 else 0
    
    return answer