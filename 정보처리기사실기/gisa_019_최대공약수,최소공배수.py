# 두 수를 입력 받아 두 수의 최대공약수와 최소공배수를 계산해서 출력하는 순서도를 작성

# 1. 일단 두 수를 입력 받아 저장 
# 2. 최대공약수로 부터 최소공배수를 계산 
    # 2-1. 최대공약수 
        # 2-1-1. 나누어 떨어지는 것들을 배열에 담는다.
        # 2-1-2. 두 배열을 비교해서 가장 큰 수를 최대공약수라고 한다. 

    # 2-2. 최소공배수 
        # 2-2-1. 최소공배수는 최대공약수의 배수? 였던 느낌인데? 
        # 2-2-2. 최대공약수를 키워나가면서 두 수로 나눠 떨어지는 처음 지점이 최소공배수로 생각. 

from re import X


print("==== 최대공약수, 최소공배수 구하기 계산기 ====")
a = int(input("처음 수 : "))
b = int(input("두 번째 수 : "))

a_list = []
b_list = []
for i in range(1,a+1):
    if a % i == 0:
        a_list.append(i)
for i in range(1,b+1):
    if b % i == 0:
        b_list.append(i)

print("a의 약수들 : " , str(a_list))
print("b의 약수들 : " + str(b_list))

# 반복문을 두번 겹쳐서 돌면서 배열안의 공통된 수 중 가장 큰 수를 찾기
x = 1 
for i in a_list:
    for j in b_list:
        if i == j:
            x = i
print("최대공약수 x : ", x)

# 최대공약수를 키워 나가면서 최소 공배수 찾기
is_stop = True
X = 0
i = 0
while is_stop:
    z = x 
    i += 1 
    z = x * i
    # print("z ", z)
    if z % a == 0 and z % b == 0 :
        X = z
        break
print("최소 공배수 X : ", X)