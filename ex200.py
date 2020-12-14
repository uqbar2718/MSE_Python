ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

profit = [] # 각 일차의 수입을 담는 리스트
revenue = 0 # 총 수익금을 계산하는 리스트


for i in ohlc[1:]: # ohlc 의 0 은 각 위치의 key 를 담고 있으므로 슬라이싱한다.
    profit.append(i[-1] - i[0]) # 각 날짜의 수익금을 profit 에 append 한다.

for i in range(len(profit)):
    revenue += profit[i] # for 문을 이용해 총 수익금을 계산한다.

revenue2 = sum(profit) # sum 함수를 이용해서 계산할 수도 있다.

print(revenue)
print(revenue2)