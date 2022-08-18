def max_sum(arr):
	maxi = 0
	current = 0
	for i in range(len(arr)):
		current = current + arr[i]
		if maxi < current:
			maxi = current
		elif current < 0:
			current = 0
	return maxi


arr = [5, 4, 6, -3, 4, -1]
print(max_sum(arr))
