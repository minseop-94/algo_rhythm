# 0 + 1 - 2 + 3 - 4 + 5 ... +99 -100 의 합계를 구하시오 
sum = 0
for i in range(100):
    if i % 2 == 0:
        i = i * -1
    sum += i

print(sum)
