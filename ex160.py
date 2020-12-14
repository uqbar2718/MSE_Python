리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in range(len(리스트)): # 리스트의 길이 만큼 for 문을 돌린다.

    ext = 리스트[i].split('.') # 확장자(EXTension)를 구분하기 위해 리스트의 각 원소들을 . 을 기준으로 split 해 준다.

    if ext[1] == 'h' or ext[1] == 'c': # 확장자가 h , c 인지 비교 해 준다.
        print(리스트[i]) # 맞다면 print 해 준다.