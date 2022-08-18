# Format
# 1. You are given a number n, representing the size of array a.
# 2. You are given n numbers, representing elements of array a.
# 3. You are given a number k.
# 4. Rotate the array a, k times to the right (for positive values of k), and to
# the left for negative values of k.

# Example
# Sample Input

# 5
# 1
# 2
# 3
# 4
# 5
# 3

# Sample Output
# 3 4 5 1 2

n = int(input())
k = int(input())

temp = n
count = 0
while temp > 0:
	temp = temp // 10
	count = count + 1

k = k % count
if k < 0:
	k = k + count

div = 1
mul = 1
for i in range(1, count+1):
	if i <= k:
		div = div * 10
	else:
		mul = mul * 10
q = n / div
r = n % div

rot = int(r * mul + q)
print(rot)
