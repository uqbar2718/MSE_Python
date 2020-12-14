
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}


ans = input("좋아하는 과일은?") # 입력 받기

if ans in fruit.values(): # fruit 딕셔너리의 value 속에 input 이 존재하는지 비교
    print("정답입니다.")# 존재하면 정답입니다 출력
else:
    print("오답입니다.")# 존재하지 않으면 오답입니다 출력

