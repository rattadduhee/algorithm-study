# 프로그래머스 lv2 - 다음 큰숫자

def solution(n):
    answer = n
    
    cnt = str(bin(n))[2:].count('1')
    while True:
        answer += 1
        if str(bin(answer))[2:].count('1') == cnt:
            break
    
    return answer