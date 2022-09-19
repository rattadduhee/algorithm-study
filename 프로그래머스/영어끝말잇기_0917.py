# 프로그래머스 lv2 - 영어끝말잇기

def solution(n, words):
    answer = []
    temp = ''
    
    for i in range(len(words)):
        if i == 0:
            temp = words[i][-1]
            continue

        if (words[:i+1].count(words[i]) > 1):  
            answer.extend(((i%n)+1, i//n +1))
            break
        if words[i][0] != temp:
            answer.extend(((i%n)+1, i//n +1))
            break

        temp = words[i][-1]
    if len(answer) == 0:
        answer = [0,0]
    
    return answer