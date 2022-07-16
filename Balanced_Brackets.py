# in this problem we will check if the string is balenced or not...
# if balenced bracket are found then we will print "true" if not then "false"
# sample output
# Input : {[]{()}}
# Output : Balanced
#
# Input : [{}{}(]
# Output : Unbalanced

from collections import deque


def isBalanced(str):
	stack = deque()
	brackets = {'(': ')', '{': '}', '[': ']'}

	for char in str:
		if char in brackets:
			stack.append(char)
		else:
			if len(stack) == 0 or char != brackets[stack.pop()]:
				return False
	p = len(stack) == 0
	return p


string = "[(a + b) + {(c + d) * (e / f)}]"

if isBalanced(string):
	print("True:- Is balanced Parenthesis")
else:
	print("False:- Is not balanced Parenthesis")
