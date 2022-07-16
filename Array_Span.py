# In this problem we will take maximum and minimum number from an array and will take difference of that

# creating an empty list
arr = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	arr.append(ele)

# arr=[10, 49, 2, 15]

max = arr[0]
min = arr[0]
for i in range(len(arr)):
	if(arr[i] > max):
		max = arr[i]
	if(arr[i] < min):
		min = arr[i]
span = max - min
print("The span in array is: ", span)