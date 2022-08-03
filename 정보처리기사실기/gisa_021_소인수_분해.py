# Q. 정수를 입력 받아 소인수를 구해 출력하는 순서도를 작성

# 소인수 : 소수인 인수

# 1. 자연수를 입력받는다
# 2. 입력받은 수의 제곱근을 구한다. 
# 3. 2부터 1씩 증가 ~제곱근까지 나누어 떨어지는지 체크
# 4-1. 나누어 떨어진다면 배열에 추가 
# 4-2. 제곱근까지 제수를 키웠는데 안떨어진다면 몫 자체가 소수..?
# 5. 몫을 소인수로 넣었을 때, 계산종료, 소인수 출력 

import math


a = int(input("소인수 분해 대상을 입력하시오 => "))
c = a
a_sqrt = int(math.sqrt(a))

x = 2
arr = [] 

while True:
    if int(c % x) == 0:
        arr.append(x)
        c = int(c / x)
        x = 1

    if x >= c:
        arr.append(c)
        arr.sort()
        print("소인수 배열: ", arr)
        break
    x += 1