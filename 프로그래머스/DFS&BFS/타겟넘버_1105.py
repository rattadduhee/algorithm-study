# DFS활용 ~!

from collections import deque
def solution(numbers, target):
    answer = 0
    d = deque()
    n = len(numbers)
    d.append([numbers[0],0])
    d.append([-numbers[0],0])
    while d:
        temp, idx = d.popleft()
        idx += 1
        if idx < n:
            d.append([temp + numbers[idx],idx])
            d.append([temp - numbers[idx],idx])
        else:
            if temp == target:
                answer +=1
            
    return answer