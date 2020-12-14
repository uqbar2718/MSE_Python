

def print_max():
    a, b, c = input("정수 3개를 입력 해 주세요.").split() # 3개의 정수를 입력 받은 후, 공백을 기준으로 split 해서 a, b, c 에 각각 배정
    a = int(a) # 이때 각 정수의 자료형은 str 이므로 이를 int 로 변경.
    b = int(b)
    c = int(c)
    
    i = 0 
    while i < 2: # 비교할 변수의 갯수가 3개이므로 비교는 최대 2회

        if c > b: # 3번째 변수와 2번째 변수를 비교하고, 둘 중 큰것을 2번째 변수로 지정.
            b, c = c, b
        if b > a: # 2번째 변수와 1번째 변수를 비교하고, 둘 중 큰 것을 1번째 변수로 지정.
            a, b = b, a

        i += 1

    print(a) # 1번째 변수를 출력.

    print_max()