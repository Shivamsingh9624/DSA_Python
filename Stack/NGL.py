
def ngl(arr):
	stack = []
	nge = [0] * len(arr)
	stack.append(arr[0])
	nge[0] = -1

	for i in range(1, len(arr)):
		while len(stack) > 0 and stack[-1] <= arr[i]:
			stack.pop()
		if len(stack) == 0:
			nge[i] = -1
		else:
			nge[i] = stack[-1]
		stack.append(arr[i])
	return nge


arr = [2, 5, 9, 3, 1, 3, 12, 6, 5, 7]
print(arr)
print(ngl(arr))
