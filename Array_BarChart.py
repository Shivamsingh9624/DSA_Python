#  in this problem we will print the Bar chart accourding to the input given

# Sample input
# 5 --- no of element
#
# 3
# 4
# 2
# 0
# 6

# output

# 				*
# 				*
# 	*			*
# *	*			*
# *	*	*		*
# *	*	*		*


n = int(input("Enter number of elements : "))
arr = []

for i in range(n):
	temp = int(input())
	arr.append(temp)

max_value = max(arr)


for floor in range(max_value, -1, -1):
	for i in range(len(arr)):
		if arr[i] >= floor:
			print("*\t")
		else:
			print("")
	print("\n")