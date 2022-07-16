import heapq


def k_smallest(arr, k):
	heap = []
	for i in range(len(arr)):
		heapq.heappush(heap, arr[i])
	heap.sort()
	return heap[k - 1]


def sum(arr, k1, k2):
	n1 = k_smallest(arr, k1)
	n2 = k_smallest(arr, k2)

	sum = 0
	for i in range(len(arr)):
		if arr[i] > n1 and arr[i] < n2:
			sum = sum + arr[i]
	return sum


arr = [20, 8, 22, 4, 12, 10, 14]
k1 = 3
k2 = 6
print(sum(arr, k1, k2))
