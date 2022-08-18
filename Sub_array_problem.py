def subarray(arr):
	ls = []
	for i in range(len(arr) + 1):
		for j in range(i):
			ls.append(arr[j: i])
	return ls


def print_array(arr):
	for i in arr:
		x = " ".join(i)
		print(x)


arr = ['10', '20', '30']
print_array(subarray(arr))
