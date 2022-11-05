# range값 잘 확인..

def solution(arr1, arr2):
    answer = [[]]

    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            cal = 0
            for k in range(len(arr2)):
                cal += (arr1[i][k] * arr2[k][j])
            temp.append(cal)
        answer.append(temp)
    answer.remove([])
    
    return answer