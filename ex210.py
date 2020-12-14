def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()


# message3 함수는 호출되었을 때 message2 함수와 C 를 각각 호출하고 print 하는 것을 3 회 반복한다.
# 그 후 message1() 함수를 한번 호출 하므로

# 결과는 BCBCBCA 일 것이다.(각 문자 사이에 줄바꿈 존재.)