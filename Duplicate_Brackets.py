# in this problem we will check if the string has duplicate bracket or nor...
# if duplicate bracket are found then we will print "true" if not then "false"
# sample output
# ((a+b) + (c+d)) --> false
# (a+b) + ((c+d)) --> true

from collections import deque

def hasDuplicateParenthesis(exp):
	if not exp or len(exp) <= 3:
		return False

	stack = deque()

	for i in exp:

		if i != ')':
			stack.append(i)
		else:
			if stack[-1] == '(':
				return True
			while stack[-1] != '(':
				stack.pop()
			stack.pop()
	return False



exp = '(a+b) + ((c+d))'

if hasDuplicateParenthesis(exp):
	print("True:- Has Duplicate parenthesis")
else:
	print("False:- Didn't found Duplicate Parenthesis")