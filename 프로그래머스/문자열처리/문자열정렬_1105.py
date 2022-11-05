# 문자열 정렬!!!!
# sorted(list_name, key = (lambda x: x[n]))

def solution(strings, n):
    answer = []
    strings.sort()
    answer = sorted(strings,key = (lambda x : x[n]))
    return answer