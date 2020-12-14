
data = [2, 4, 3, 1, 5, 10, 9]

data.sort() # 방법 1. sort 는 리스트를 오름차순/내림차순(reverse = True)으로 정렬할 수 있는 메서드이다. 
print(data)



data2 = [2, 4, 3, 1, 5, 10, 9]

data2 = sorted(data2) # 방법 2. sorted 함수는 순서대로 정렬된 리스트를 반환하는 함수이다.
print(data2)



data3 = [2, 4, 3, 1, 5, 10, 9] # 방법 3. 반복문을 이용한다.

for i in range(len(data3)): 
	
	for j in range(len(data3) - i): # i 번째 원소 다음에 i 번째 원소보다 작은 원소가 있으면, 그 원소와 i 번째 원소를 교환한다.

		if data3[i] > data3[j + i]:
			data3[j + i], data3[i] =  data3[i], data3[j + i]
			
print(data3)


