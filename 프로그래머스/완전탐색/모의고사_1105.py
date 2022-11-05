def solution(answers):
    answer = []
    ans = {1:[1, 2, 3, 4, 5], 2:[2, 1, 2, 3, 2, 4, 2, 5], 3:[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    correct = [0,0,0]
    
    for i in ans:
        l = len(ans[i])
        for j in range(0,len(answers),l):
            if j+l > len(answers):
                temp = answers[j:]
            else:
                temp = answers[j:j+l]
                
            for k in range(len(temp)):
                if ans[i][k] == temp[k]:
                    correct[i-1] += 1
    for i in range(len(correct)):
        if correct[i] == max(correct):
            answer.append(i+1)
    answer.sort()
    return answer