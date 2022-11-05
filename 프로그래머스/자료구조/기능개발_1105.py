# 올림 : math.ceil 활용
# 내림 : math.floor

import math

def solution(progresses, speeds):
    answer = []
    temp = []
    for i in range(len(progresses)):
        cal = math.ceil((100 - progresses[i])/speeds[i])
        if len(temp)==0:
            temp.append(cal)
            continue
        if temp[0] >= cal:
            temp.append(cal)
        else:
            answer.append(len(temp))
            temp = [cal]
    answer.append(len(temp))
    return answer