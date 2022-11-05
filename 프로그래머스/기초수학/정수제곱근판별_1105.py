# math 함수를 활용한 sqrt

import math as m
def solution(n):
    answer = 0
    num = m.sqrt(n)
    if num % 1 == 0:
        answer = (num+1)**2
    else:
        answer = -1
    return answer