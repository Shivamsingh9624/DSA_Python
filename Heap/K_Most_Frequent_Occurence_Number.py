import heapq


def pr_N_mostFrequentNumber(arr, n, k):
	mp = {}
	for i in range(n):
		if arr[i] in mp:
			mp[arr[i]] += 1
		else:
			mp[arr[i]] = 1

	# heap = [(value, key) for key, value in mp.items()]
	heap = []
	for key, value in mp.items():
		heap.append((value, key))
	largest = heapq.nlargest(k, heap)
	print(k, " numbers with most " "occurrences are:", sep="")

	for i in range(k):
		print(largest[i][1], end=" ")


arr = [3, 1, 1, 1, 1, 1, 4, 4, 6, 2, 1, 3, 4, 3, 2, 2, 2, 4, 5, 5, 2, 6, 1]
n = len(arr)
k = 2
pr_N_mostFrequentNumber(arr, n, k)
