# Format
# Input
# A number n
# n1
# n2
# .. n number of elements
#
# Output
# A number representing max - min
#
# Example
# Sample Input
#
# 6
# 15
# 30
# 40
# 4
# 11
# 9
#
# Sample Output
# 36


arr = []

n = int(input("Enter number of elements : "))

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