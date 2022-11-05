def solution(citations):
    n = max(citations)
    citations.sort(reverse=True)
    
    while True:
        answer = 0
        for i in citations:
            if i >= n:
                answer += 1
            else:
                break
        if answer >= n:
            return n
        else:n -= 1
