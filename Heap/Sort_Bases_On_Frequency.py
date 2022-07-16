import heapq
# write your code here
def solve(string):
	heap = []
	mp = {}
	for i in string:
		if i in mp:
			mp[i] += 1
		else:
			mp[i] = 1

	for key, values in mp.items():
		heap.append((values, key))

	heapq._heapify_max(heap)
	print("Most frequent occured character is: ", heap[0][1], "That is ", heap[0][0], "Times")

string = "zmszeqxllzvheqwrofjenhdwkejdcbsbjkdhccjkdbcjsmcgcuntypejcxovtaqbnqyqlmrwitc"
solve(string)