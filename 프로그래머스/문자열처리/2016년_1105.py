def solution(a, b):
    answer = ''
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    temp = 0
    for i in range(1,a):
        if i in [1,3,5,7,8,10,12]:
            temp += 31
        elif i == 2:
            temp += 29
        else:
            temp += 30

    b = (temp + b - 1) % 7
    answer = day[b]
    return answer