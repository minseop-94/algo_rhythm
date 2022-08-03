# 임의의 정수를 입력 받아 그 안에 포함된 소수의 합을 구하는 프로그램 작성

# 1. 16과 같은 방식으로 소수인지 체크
# 2. 소수라면 합칠 변수 하나 sum

import math


a = int(input("임의의 정수를 입력 => "))
sum = 5

if a == 2 :
    print("a까지의 소수 합: 2")

if a == 3 :
    print("a까지의 소수 합: 3")
    
x = 2
for i in range(4, a+1):
    while True:
        if i % x == 0:
            break
        if i % x != 0:
            x += 1
        if x == i:
            sum += i
            x = 2
            break

    print("i : " , i)

if a != 2 or a != 3:
    print("a까지의 소수 합: ", sum)
    print("시스템 종료!!!")