# Format
# Input
# A String
#
# Output
# All permutations of the given string(one in a line).
#
# Example
# Sample Input
#
# abc
#
# Sample Output
# abc
# bac
# cab
# acb
# bca
# cba

def solution(s):
	sub = []
	for i in range(len(s)):
		for j in range(i + 1, len(s) + 1):
			sub.append(s[i:j])
	return sub

s = "abc"
print(solution(s))