def check(expression):
    stack = []
    exp = ['(','{','[']
    closing_exp = [')', '}', ']']
    for i in expression:
        if i in exp:
            stack.append(i)
        else:
            if i in closing_exp:
                pos = closing_exp.index(i)
                if len(stack) > 0 and (exp[pos] == stack[len(stack)-1]):
                    stack.pop()
                else:
                    print("false")
                    return
    if len(stack) == 0:
        print('true')
    else:
        print('false')
expression = "[(a + b) + {(c + d) * (e / f)]}"
check(expression)

sts = 'zmszeqxllzvheqwrofgcuntypejcxovtaqbnqyqlmrwitc'
print(''.join(sorted(sts)))
# print(sts)

