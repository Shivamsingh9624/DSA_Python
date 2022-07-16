

def nge(arr):
	stack = []
	nge = [0] * len(arr)
	stack.append(arr[len(arr) - 1])
	nge[len(arr)-1] = -1

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
print(nge(arr))