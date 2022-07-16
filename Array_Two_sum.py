# in this program we will make the sum of two arrays

# a1
# 3
# 2
# 2
# 2
# a2
# 4
# 1
# 1
# 1
# 1

# Output
# 1 3 3 3

# explanation
# 1 1 1 1
#   2 2 2
# --------
# 1 3 3 3

a1 = []
a2 = []
print("enter the elements of both array after writing the elements of first array: ")

a = int(input())
for i in range(a):
	temp = int(input())
	a1.append(temp)

b = int(input())
for j in range(b):
	temp = int(input())
	a2.append(temp)



size = a if a > b else b
sum = [0] * size

carry = 0

i = len(a1) - 1
j = len(a2) - 1
k = len(sum) - 1

while k >= 0:
	d = int(carry)

	if i >= 0:
		d += a1[i]
	if j >= 0:
		d += a2[j]

	carry = int(d / 10)
	d = int(d % 10)

	sum[k] = d

	i -= 1
	j -= 1
	k -= 1


if carry != 0:
	print(carry)
for val in sum:
	print(val)
