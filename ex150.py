list1 = ["가", "나", "다", "라"]
list2 = ["가", "나", "다", "라"]
list3 = ["가", "나", "다", "라"]


# 방법 1. reverse() 메서드를 활용하여 리스트를 뒤집고 반복문을 이용, print 한다.
list1.reverse() # reverse() 메서드: 리스트에 있는 값의 순서를 거꾸로 뒤집는다.
print('방법1')
for i in range(len(list1)):
    print(list1[i])


print('\n')


print('방법2')# 방법 2. reversed() 메서드를 활용하여 리스트를 뒤집고 반복문을 이용, print 한다. 

for j in (reversed(list2)): #reversed() 메서드: 값의 순서가 거꾸로 되집힌 리스트를 리턴한다.
    print(j)


print('\n')


print('방법3')# 방법 3. 리스트 슬라이싱을 이용한다.

for k in list3[: : -1]: # 증감폭이 음수라면 리스트는 역순으로 참조가 된다.
    print(k)