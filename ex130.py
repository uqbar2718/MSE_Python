
import requests #requests 모듈을 import 하기 전 pip3 install requests 를 입력해서 requests 모듈을 설치 하도록 하자.

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] #비트코인의 가격 정보를 딕셔너리로 가져오는 코드

fluct = int(btc['max_price']) - int(btc['min_price']) # 변동폭(Stock Fluctuation)을 최고가와 최저가의 차로 정의, 이때 btc 의 value의 자료형은 str 이므로 이를 int 로 변환

if int(btc['opening_price']) + fluct > int(btc['max_price']) : # 시가 + 변동폭이 최고가보다 높은지 비교
    print('상승장')
else:
    print('하락장')

