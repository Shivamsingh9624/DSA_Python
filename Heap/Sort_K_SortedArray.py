# here we are given a k sorted array...that means the element is present inside the k range only

# normally sorting take time complexity of nlogn
# now by using heap we will be able to sort this in time complexity of nlogk
# input: [6,5,3,2,8,10,9] k=3
# output: [2,3,5,6,8,9,10]

# from heapq import heapify, heappush, heappop
import heapq

def sorting(arr, k):
	minheap = []
	for i in range(k + 1):
		heapq.heappush(minheap, arr[i])
	# heapify(minheap)
	index = 0
	for k in range(k + 1, len(arr)):
		arr[index] = heapq.heappop(minheap)
		heapq.heappush(minheap, arr[k])
		index += 1
	while minheap:
		arr[index] = heapq.heappop(minheap)
		index += 1


def print_array(arr: list):
	for elem in arr:
		print(elem, end=' ')


arr = [2, 6, 3, 12, 56, 8]
k = 3
sorting(arr, k)
print('Following is sorted array')
print_array(arr)
