
nums = [1, 2, 3, 4, 5]

avg1 = sum(nums)/len(nums) #방법 1. sum 함수를 이용해 리스트의 총 합을 구한 후 len 함수를 이용해 리스트의 원소의 갯수로 나눈다.

print(avg1)


sums = 0
leng = 0
for i in range(len(nums)): # 방법 2. 반복문을 이용해 리스트의 총 합과 길이를 구하고, 이를 이용해 평균을 구한다.
	sums += nums[i]
	leng += 1

avg2 = sums/leng
print(avg2)