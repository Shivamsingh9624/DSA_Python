# 1. You are given a number n, representing the size of array a.
# 2. You are given n numbers, representing elements of array a.
# 3. You are given a number k.
# 4. Rotate the array a, k times to the right (for positive values of k), and to
# the left for negative values of k.

# Sample Input
#
# 5
# 1
# 2
# 3
# 4
# 5
# 3
#
# Sample Output
# 3 4 5 1 2

# def reverse(i, j):
# 	li = i
# 	ri = j
# 	while li < ri:
# 		temp = arr[li]
# 		arr[li] = arr[ri]
# 		arr[ri] = temp
# 		li += 1
# 		ri -= 1


# def rotate(k):
# 	k = k % len(arr)
# 	if k < 0:
# 		k = k + len(arr)
# 	reverse(0, len(arr) - k - 1)
# 	reverse(len(arr) - k, len(arr) - 1)
# 	reverse(0, len(arr) - 1)
#
# 	return arr


def rotate(arr,k):
	l = len(arr)
	k = k % l
	if k and l > 1:
		arr[:k], arr[k:] = arr[-k:], arr[:-k]
	return arr


a = int(input())
arr = []
for i in range(a):
	temp = int(input())
	arr.append(temp)

k = int(input())
print(rotate(arr,k))
