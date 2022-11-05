def solution(people, limit):
    answer = 0    
    people.sort()
    
    while people:
        temp = people.pop()
        if len(people)!=0:
            while (temp+people[0])<=limit:
                temp += people[0]
                del people[0]
        answer += 1
    
    return answer