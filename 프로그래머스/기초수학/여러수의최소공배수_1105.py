# 두 수 a, b의 최대공약수 gcd
# 두 수 a, b의 최소공배수 lcm = (a * b) // gcd

# 세 수 a, b, c의 최대공약수 = 두 수 a, b의 최대공약수인 g와 c의 최대공약수 gcd
# 세 수 a, b, c의 최소공배수 = 두 수 a, b의 최소공배수인 l과 c의 최소공배수 lcm

def solution(arr):
    a = arr.pop()
    while arr:
        b = arr.pop()
        cal = a*b
        if a>b:
            a,b = b,a
        while b%a:
            a,b = b%a,a
        a = cal/a
    return a