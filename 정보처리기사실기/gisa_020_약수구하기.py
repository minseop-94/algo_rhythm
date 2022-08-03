# 정수를 입력 받아 약수를 구해 출력하는 순서도를 작성.

# 이거 아까 최대공약수에서 했던거...아냐? 

a = int(input("정수를 입력해주세요 : "))
a_list = []
for i in range(1,a+1):
    if a % i == 0:
        a_list.append(i)

print(a_list)