def solution(priorities, location):
    answer = 0
    while len(priorities) > 0:
        if priorities[0] == max(priorities):
            answer += 1
            if location == 0:
                break
            priorities.pop(0)
            location -= 1
        else:
            temp = priorities.pop(0)
            priorities.append(temp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer