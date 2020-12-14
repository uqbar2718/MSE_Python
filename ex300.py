per = ["10.31", "", "8.00"]

for i in per:
    try: # 가장 먼저 실행해볼 코드
        print(float(i))
    except: # 오류가 발생했을 때 수행할 코드
        print(" ") 
    else: # 예외가 발생하지 않았을 때 수행할 코드
        print("else")
    finally: # 최종적으로 수행할 코드
        print(" final ")





