# 백준 - 그리디 1744번 - 수 묶기

n = int(input())
num1 = []
num2 = []
temp = 0
result = 0

for _ in range(n):
    k = int(input())
    if k > 0 :
        num1.append(k)
    else:
        num2.append(k)

# 정렬
num1.sort(reverse=True)   # [5,4,3,1] : 역순정렬
num2.sort()               # [-5,-4,-3,-1] : 정렬

if len(num1) >= 1:
    temp = num1.count(1)  # 1개수 저장

    # 1이 있을 경우, 1 제외 후 계산
    if 1 in num1:
        # 1의 제외한 숫자의 개수가 짝수일 때
        if len(num1) > temp and (len(num1)-temp) % 2 == 0:
            for i in range(0, len(num1) - temp, 2):
                result += num1[i] * num1[i+1]
            result += temp
        # 1의 제외한 숫자의 개수가 홀수일 때
        elif len(num1) > temp and (len(num1)-temp) % 2 != 0:
            for i in range(0, len(num1) - (temp + 1), 2):
                result += num1[i] * num1[i+1]
            result += num1[-(temp+1)] + temp
        # 1밖에 없을 경우
        else:
            result += temp
    # 1이 없을 경우, 차례로 계산
    else:
        if len(num1) % 2 == 0:
            for i in range(0, len(num1), 2):
                result += num1[i] * num1[i+1]
        else:
            for i in range(0, len(num1) - 1, 2):
                result += num1[i] * num1[i+1]
            result += num1[-1]

if len(num2) >= 1:
    temp = num2.count(0)  # 0개수 저장
    # 0이 있을경우
    if 0 in num2:
        if len(num2)>temp and (len(num2)-temp) % 2 == 0:
            for i in range(0, len(num2)- temp, 2):
                result += num2[i] * num2[i+1]
        
        elif len(num2)>temp and (len(num2)-temp) % 2 != 0:
            for i in range(0, len(num2)- temp -1, 2):
                result += num2[i] * num2[i+1]
            
    # 0이 없을 경우
    else:
        if len(num2) % 2 == 0:
            for i in range(0, len(num2), 2):
                result += num2[i] * num2[i+1]
        else:
            for i in range(0, len(num2) -1, 2):
                result += num2[i] * num2[i+1]
            result += num2[-1]
    

print(result)