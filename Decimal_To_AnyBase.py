# 1. You are given a decimal number n.
# 2. You are given a base b.
# 3. You are required to convert the number n into its corresponding value in base b.

# Input
# A number n
# A base b
#
# Output
# A number representing corresponding value of n in number system of base b

# Sample Input
#
# 57
#  2
#
# Sample Output
# 111001

def getValueInBase(d, c):
	rv = 0
	p = 1
	while d > 0:
		dig = d % c
		d = d // c

		rv += dig * p
		p = p * 10
	return rv


d = int(input())
c = int(input())
print(getValueInBase(d, c))
