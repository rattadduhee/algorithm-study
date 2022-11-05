# len으로 정렬하기
def solution(s):
    answer = []
    temp = list(s.split('},{'))
    for i in range(len(temp)):
        temp[i] = temp[i].strip('{}')
        temp[i] = list(map(int,temp[i].split(',')))
    temp = sorted(temp, key = lambda x : len(x))   
    
    for i in temp:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer