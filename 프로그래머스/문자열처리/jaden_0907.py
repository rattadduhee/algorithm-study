# 프로그래머스 JadenCase 문자열 만들기
# lower, upper 함수 활용

def solution(s):
    answer = ''
    
    a = list((s.lower()).split(' '))
    
    for i in range(len(a)):
        for j in range(len(a[i])): 
            if a[i][j] != '':
                answer += a[i][j].upper() + a[i][j+1:]
                break
         
        answer += ' ' if i != (len(a) -1) else ''
    
    return answer