# 백준 1260번 - 그래프 - DFS와 BFS
from collections import deque

def DFS(n, start, g):
    res = deque()
    d = [0] * (n+1)
    
    res.append(start)
    d[start] = 1




    return res

def BFS(n, start, g):
    res = deque()
    d = [0] * n
    return res

n, m, v = map(int, input().split())
graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))

print(DFS(n, v,graph))
print(BFS(n, v,graph))

