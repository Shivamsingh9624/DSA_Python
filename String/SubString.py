# 1. You are given a string.
# 2. You have to print all palindromic substrings of the given string.

# Example
# Sample Input
# abcc

# Sample Output
# a
# b
# c
# cc
# c

# For palindrome
def isPallindrome(st):
	if st == st[::-1]:
		return True
	else:
		return False


# Get all substrings of string using list comprehension and string slicing
s = 'abcc'
sub = []
for i in range(len(s)):
	for j in range(i + 1, len(s) + 1):
		sub.append(s[i:j])

# printing palindrome string
for i in sub:
	if isPallindrome(i):
		print(i)

isPallindrome(sub)
