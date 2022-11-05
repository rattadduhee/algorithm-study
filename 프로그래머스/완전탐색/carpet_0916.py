# 프로그래머스 lv2 - 완전탐색 - 카펫

def solution(brown, yellow):
    answer = []
    
    ans = brown + yellow
    for i in range(3, ans):
        if ans % i == 0:
            if (i-2) * ((ans // i)-2) == yellow:
                answer.append(i)
                answer.append(ans//i)
                break
                
    answer.sort(reverse=True)
    return answer