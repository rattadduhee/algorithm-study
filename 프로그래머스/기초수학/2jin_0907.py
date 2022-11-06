# 프로그래머스 이진변환 반복하기
# count, replace, bin 등 함수 활용

def solution(s):
    answer = [0,0]

    while int(s) > 1:
        answer[1] += s.count('0')
        s = s.replace('0','')
        s = bin(len(str(s)))[2:]
        answer[0]+=1
    
    return answer