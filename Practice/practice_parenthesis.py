# stack = []
#
# str = "}"
# open_brackets = ['(', '{', '[']
# close_brackets = [')', '}', ']']
#
# for char in str:
# 	if char in open_brackets:
# 		stack.append(char)
# 	elif char in close_brackets:
# 		pos = close_brackets.index(char)
# 		if len(stack) > 0 and (open_brackets[pos] == stack[len(stack) - 1]):
# 			stack.pop()
# 		else:
# 			print("Unbalanced")
# 			break
#
# if len(stack) == 0:
# 	print("Balanced")
# else:
# 	print("Unbalanced")

def is_match(p1, p2):
	if p1 == '(' and p2 == ')':
		return True

	elif p1 == '{' and p2 == '}':
		return True

	elif p1 == '[' and p2 == ']':
		return True

	else:
		return False


def isBalanced(str):
	stack = []
	is_balanced = True
	index = 0

	while index < len(str) and is_balanced:
		paren = str[index]
		if paren in "({{":
			stack.append(paren)
		else:
			if len(stack) == 0:
				is_balanced = False
			else:
				top = stack.pop()
				if not is_match(top, paren):
					is_balanced = False
		index += 1
	if len(stack) == 0 and is_balanced and str != "":
		return True
	else:
		return False

print(isBalanced("(}{)"))
