low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = [] # 변동폭을 담기 위한 빈 리스트 생성.


for i in range(len(low_prices)): # low_prices 리스트의 길이 만큼 반복문을 돌림.
    volatility.append(high_prices[i] - low_prices[i]) # i 일의 고가와 저가의 차를 i 일의 변동폭으로 추가.

print(volatility)