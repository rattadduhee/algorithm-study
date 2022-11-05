def solution(operations):
    answer = []
    for i in operations:
        s = i.split(' ')
        if s[0] == 'I':
            answer.append(int(s[1]))
        elif s[0] == 'D':
            if len(answer) == 0:
                continue
            elif s[1] == '1':
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
    answer.sort(reverse=True)
    if len(answer)>2:
        answer = [max(answer), min(answer)]
    elif len(answer) == 0:
        answer = [0,0]
    return answer