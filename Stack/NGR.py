# Find the next greater element to the right
# This can be done using the stack
# The operation (POP - ANSWER - PUSH) is to be done

# Format
# Input
# Input is managed for you
#
# Output
# Output is managed for you
#
# Example
# Sample Input
#
# 5
# 5
# 3
# 8
# -2
# 7
#
# Sample Output
# 8
# 8
# -1
# 7
# -1

def ngr(arr):
	stack = []
	nge = [0] * len(arr)
	nge[len(arr) - 1] = -1
	stack.append(arr[len(arr) - 1])
	for i in range(len(arr) - 2, -1, -1):
		while len(stack) > 0 and arr[i] >= stack[-1]:
			stack.pop()
		if len(stack) == 0:
			nge[i] = -1
		else:
			nge[i] = stack[-1]
		stack.append(arr[i])
	return nge


arr = [9, 1, 3, 7, 4, 2, 8, 6, 3, 8]
print(arr)
# print("Next Greater Element Are As Given")
print(ngr(arr))
