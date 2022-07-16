# in this problem we will take input from user and find if the element is present in which array or nor....if present print the index value
# Sample input:
# 3 ---- no of element
# 12
# 24
# 45
# 24 ---- element to be found
# Output
# 2


n = int(input("Enter number of elements : "))
arr = []

for i in range(n):
	temp = int(input())
	arr.append(temp)


find = int(input())

index = -1
for j in range(len(arr)):
	if(arr[j] == find):
		index = j
		break

print(index + 1)

