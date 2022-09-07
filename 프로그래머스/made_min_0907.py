# 프로그래머스 최솟값 만들기
# 효율성 테스트로 인한 재귀함수 및 내장함수 활용 줄이기

def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        answer += A[len(A)-i-1] * B[i]
    
    return answer



#def solution(A,B):
#    answer = 0
#     for i in range(len(A)): 
#         answer += min(A) * max(B)
#         A.remove(min(A))
#         B.remove(max(B))
#     return answer