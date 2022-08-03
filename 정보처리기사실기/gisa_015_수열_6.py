# 1+1+2+3+5+8+13+.. 의 순서로 나열되는 
# 피보나치 수열의 20번째 항까지의 합꼐를 구하시오 

# 첫항 a, 두번째 b, 세번째 c , 반복 변수 i, 누적합 변수 sum 
#

a = 1
b = 1 
c = 0
sum = 2

for i in range(2,20):
    print("i : ", i)
    c = a + b
    sum += c 
    a = b 
    b = c 

    

print("answer : ", sum)