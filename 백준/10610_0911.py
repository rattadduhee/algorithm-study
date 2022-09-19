# 백준 - 그리디 10610번 - 30
# 입력받은 숫자를 이용해서 30의 배수 중 가장 큰 수 만들기
# 입력받은 수에서 0을 제외한 나머지 숫자의 합이 3의 배수

num = input()
arr = []
count = 0

for i in range(len(num)):
    arr.append(num[i])

arr.sort(reverse = True)

if '0' not in arr:
    print(-1)
else:
    for i in arr:
        count += int(i)
    if count % 3 == 0:
        print(int(''.join(arr)))
    else: print(-1)