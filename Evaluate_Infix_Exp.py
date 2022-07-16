# in this problem we will evaluate the infix expression and find the answer of the same
# input: 3+2/5*2
# output: 8

def precedence(optor):
	if optor == '+':
		return '1'
	elif optor == '-':
		return '1'
	elif optor == '*':
		return '2'
	else:
		return '2'


def operation(v1, v2, optor):
	if optor == '+':
		return int(v1 + v2)
	elif optor == '-':
		return int(v1 - v2)
	elif optor == '*':
		return int(v1 * v2)
	else:
		return int(v1 / v2)
# -------------------------Main Code--------------------


from collections import deque

opnts = []
optors = []

# print(len(optors))

exp = "3+2+5/2"

for i in range(len(exp)):
	ch = exp[i]
	if ch == '(':
		optors.append(ch)
	elif ch.isdigit():
		val = 0
		val = (val * 10) + int(ch)
		opnts.append(val)
	elif ch == ')':
		while optors[-1] != '(':
			optor = optors.pop()
			v2 = opnts.pop()
			v1 = opnts.pop()
			opv = operation(v1, v2, optor)
			opnts.append(opv)
		optors.pop()

	elif ch == '+' or ch == '-' or ch == '*' or ch == '/':
		while len(optors) > 0 and optors[-1] == '(' and precedence(ch) <= optors[-1]:
			optor = optors.pop()
			v2 = opnts.pop()
			v1 = opnts.pop()
			opv = operation(v1, v2, optor)
			opnts.append(opv)
		optors.append(ch)

while len(optors) != 0:
	optor = optors.pop()
	v2 = opnts.pop()
	v1 = opnts.pop()
	opv = operation(v1, v2, optor)
	opnts.append(opv)
# optors.pop()

print(opnts[-1])

