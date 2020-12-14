class OMG : 
    def print() : # 메서드의 첫 번째 매개변수 self 가 존재하지 않아 객체의 호출이 올바르게 이루어지지 않는다.
    # def print(self): # 라 하면 올바르게 결과가 출력되는 것을 볼 수 있다.
        print("Oh my god")

mystock = OMG()
mystock.print()