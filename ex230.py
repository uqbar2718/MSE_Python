def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

# 함수를 지정할 때 사용한 변수 a, b 와, 함수를 호출할 때 사용한 변수 a, b 는 이름은 같지만 종류가 다르므로,
# 왼쪽 100, 오른쪽 200 이 출력될 것 이다. (오답)

# 해설참고) a 변수에 200, b 변수에 100을 바인딩 하라 지정이 되어 있으므로, 왼쪽 200, 오른쪽 100이 출력 되게 된다.
