def solution(n, lost, reserve):
    answer = 0
    cal = n - len(lost)
    lost.sort()
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            cal += 1
        elif (i-1) in reserve:
            if i-1 in lost:
                continue
            reserve.remove(i-1)
            cal += 1
        elif (i+1) in reserve:
            if i+1 in lost:
                continue
            reserve.remove(i+1)
            cal += 1
    
    answer = cal
    return answer