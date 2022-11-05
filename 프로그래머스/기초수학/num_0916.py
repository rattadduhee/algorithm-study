# 프로그래머스 lv2- 숫자의 표현

def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            if i % 2 == 1:
                answer += 1
        
    return answer

num = int(input())
solution(num)



# len([i  for i in range(1,num+1,2) if num % i is 0])