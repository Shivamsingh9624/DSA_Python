def solution(st):
	s = st[0]
	for i in range(1, len(st)):
		current = st[i]
		previous = st[i - 1]
		gap = ord(current) - ord(previous)
		s += str(gap)
		s += current
	return s

st = "pepCODinG"
print(solution(st))