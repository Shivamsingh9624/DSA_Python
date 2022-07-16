import heapq

def minimize(arr):
	heapq.heapify(arr)
	cost = 0
	while(len(arr) >= 2):
		a = heapq.heappop(arr)
		b = heapq.heappop(arr)
		# print("Value of a is", a)
		# print("Value of b is", b)
		cost = cost + a + b
		# print("Value of cost is", cost)
		heapq.heappush(arr, a + b)
	return cost

arr = [5, 4, 2, 8] #9 + 11 + 29 = 49
print("Total cost for connecting ropes is: ", minimize(arr))
