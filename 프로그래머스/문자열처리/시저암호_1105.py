# 프로그래머스 - 문자열 활용
# find 함수 -> 특정 문자열이 포함된 index 값 반환

def solution(s, n):
    answer = ''
    
    for i in list(s):
        temp = 'abcdefghijklmnopqrstuvwxyz'
        if i != i.lower():
            temp = temp.upper()
        if i == ' ':
            answer += i
            continue
        t = temp.find(i)
        if t+n > len(temp)-1:
            answer += temp[t+n-len(temp)]
        else:
            answer += temp[t+n]
    return answer