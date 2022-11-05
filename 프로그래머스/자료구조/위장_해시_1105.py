# defaultdict를 활용한 조합구현

from collections import defaultdict

def solution(clothes):
    answer = 1
    dic = defaultdict(list)
    
    for item, key in clothes:
        dic[key].append(item)
        
    for key in dic.keys():
        answer *= len(dic[key])+1
    answer -= 1
    
    return answer