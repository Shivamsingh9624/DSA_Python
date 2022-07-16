import heapq


def k_largestelement(arr, k):
	minheap = []
	for i in range(k):
		heapq.heappush(minheap, arr[i])
	for k in range(k + 1, len(arr)):
		if arr[k] > minheap[0]:
			heapq.heappop(minheap)
	return minheap


arr = [3, 4, 7, 10, 15, 20]
k = 3
print(k_largestelement(arr, k))
