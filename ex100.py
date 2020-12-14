
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price)) # zip 함수는 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 한다.

print(close_table)