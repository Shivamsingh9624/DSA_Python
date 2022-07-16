# import heapq
# listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# heapq.heapify(listForTree)             # for a min heap
# heapq._heapify_max(listForTree)        # for a maxheap!!

# If you then want to pop elements, use:

# heapq.heappop(minheap)      # pop from minheap
# heapq._heappop_max(maxheap) # pop from maxheap

import heapq


def solve(arr):
	mp = {}
	for i in range(len(arr)):
		if arr[i] in mp:
			mp[arr[i]] += 1
		else:
			mp[arr[i]] = 1
	heap = []
	for key, values in mp.items():
		heap.append((values, key))
	heapq._heapify_max(heap)

	ans = []
	for i, j in heap:
		for l in range(i):
			ans.append(j)

	return ans


arr = [1, 1, 3, 3, 4, 4, 5, 5, 2, 2, 1, 1, 3, 3, 3, 3, ]
print(solve(arr))
