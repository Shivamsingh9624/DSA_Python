# 1. You are given an ArrayList of positive integers.
# 2. You have to remove prime numbers from the given ArrayList and return the updated ArrayList.
# Note -> The order of elements should remain same.

# Here We have to start loop from the end of the list....because if we remove element from the starting of the list
# then next element will be skipped and soo we will get the error "Index out of range"

# Input
# A number N arr1 arr2.. N numbers

# Output
# An Arraylist

# Example
# Sample Input
# 4
# 3 12 13 15

# Sample Output
# [12, 15]

def isPrime(n):
	if n > 1:
		for i in range(2, int(n / 2) + 1):
			if n % i == 0:
				return False
	return True


def solution(al):
	for i in range(len(al)-1, -1, -1):
		# print(al[i])
		if isPrime(al[i]):
			al.remove(al[i])
	return al


al = [3, 12, 13, 15]
solution(al)
print(al)
