# using array

def rain_water_trap(arr):
	right = [0] * len(arr)
	right[-1] = arr[-1]
	left = [arr[0]]
	for i in range(len(arr) - 1):
		temp = max(left[i], arr[i])
		left.append(temp)

	for j in range(len(arr)-1, -1, -1):
		temp = max(right[j], arr[j])
		right[j] = temp
	print(left)
	return right


arr = [3, 1, 2, 4, 0, 1, 3, 2]
print(rain_water_trap(arr))
