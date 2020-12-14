class Stock: # 클래스 Stock 정의
    def setdata(self, name, code, PER, PBR, divYield): # 클래스의 요소 정의
        self.name = name # 종목명
        self.code = code # 종목코드
        self.PER = PER # PER
        self.PBR = PBR # PBR
        self.divYield = divYield # 배당수익율


삼성 = Stock() # 객체 '삼성' 생성
삼성.setdata("삼성전자", "005930", 15.79, 1.33, 2.83) # 삼성 객체에 대한 각 값 대입

현대 = Stock() # 객체 '현대' 생성
현대.setdata('현대차', '005380', 8.70, 0.35, 4.27)  # 현대 객체에 대한 각 값 대입

LG = Stock() # 객체 'LG' 생성
LG.setdata('LG전자', '066570', 317.34, 0.69, 1.37) # LG 객체에 대한 각 값 대입

Stocks = [삼성, 현대, LG] # 세 객체를 담는 리스트 생성

for i in Stocks: # 종목코드와 PER 을 출력하는 반복문
    print(i.code, i.PER)