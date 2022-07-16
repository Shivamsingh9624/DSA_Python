from heapq import heappop, heappush


def findkthsmallest(nums, k):
	maxHeap = []
	for i in range(k + 1):
		heappush(maxHeap, nums[i])
	for i in range(k + 1, len(nums)):
		if nums[i] > maxHeap[0]:
			heappop(maxHeap)
		# heappush(maxHeap, nums[i])
	return maxHeap[0]


var = [6, 4, 9, 3, 1]
k = 2
print(findkthsmallest(var, k))
