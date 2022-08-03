# 10진수를 입력 받아 2진수로 변환하는 순서도를 작성 하시오. 단 1000 이하의 숫자를 입력 받는다. 

# 10을 입력받는다
# 2로 나눈다(2진수)
# 나머지를 배열에 저장한다
# 몫을 다시 나눈다. 
# 위의 과정을 반복해서 몫이 1이하로 떨어질때
# 배열을 거꾸로 출력한다. 

a = int(input("2진수 변환기 => "))
arr = []
i = 1 # test용 
while True:

    if a < 2: # 2로 나누다가 2보다 작을때 끝!! 
        arr.append(a)
        print("마지막 배열", arr)
        arr.reverse()
        print("거꾸로 배열", arr)
        x = ""
        for i in arr:
            x += str(i)
        print("2진수 : " + x)
        break
    # 2진수 변환식 -> 2로 나누고 나머지를 배열에 저장, 몫은 다음에 쓴다 
    a_namaji = a % 2 
    
    print(f"{i}번 나머지: ", a_namaji)
    a = int(a / 2)
    print(f"{i}번 몫: ", a)
    i += 1
    arr.append(a_namaji)
    print(f"{i}번 배열", arr)

    