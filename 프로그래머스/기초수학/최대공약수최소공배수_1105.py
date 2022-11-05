def solution(n, m):
    temp = n*m
    if n>m:
        n, m = m, n
    while m%n:
        n,m = m%n, n
    return [n, temp/n]