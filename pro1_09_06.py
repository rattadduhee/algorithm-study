# 프로그래머스 1단계 - 성격 유형 검사하기

arr = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}

def solution(survey, choices):
    answer = ''

    for i in range(len(survey)):
        if choices[i] > 4: 
            arr[survey[i][1]] += score[choices[i]]
        else:
            arr[survey[i][0]] += score[choices[i]]

    answer += 'R' if arr['R'] >= arr['T'] else 'T'
    answer += 'C' if arr['C'] >= arr['F'] else 'F'
    answer += 'J' if arr['J'] >= arr['M'] else 'M'
    answer += 'A' if arr['A'] >= arr['N'] else 'N'

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))