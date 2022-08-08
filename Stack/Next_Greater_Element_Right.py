# in this problem we will find the next greater element in he right side in an given array
# Here the Rule "-(pop), answer, +{push)" rule is used
# input:- 9 2 3 6 2 3 5 2
# output:-1 3 6 -1 3 5 -1 -1

def solve(arr):
	stack = []
	nge = [0] * len(arr)
	stack.append(arr[len(arr) - 1])
	nge[len(arr) - 1] = -1

	for i in range(len(arr) - 2, -1, -1):
		while len(stack) > 0 and arr[i] >= stack[-1]:
			stack.pop()
		if len(stack) == 0:
			nge[i] = -1
		else:
			nge[i] = stack[-1]
		stack.append(arr[i])

	return nge


arr = [7, 2, 4, 6, 2, 1, 13, 4, 6, 7, 6, 4, 5]
print(arr)
print(solve(arr))
