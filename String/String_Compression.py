def compression1(st):
	s = st[0]
	for i in range(1, len(st)):
		current = st[i]
		previous = st[i - 1]
		if current != previous:
			s += st[i]
	return s


def compression2(st):
	s = st[0]
	count = 1
	for i in range(1, len(st)):
		current = st[i]
		previous = st[i - 1]
		if current == previous:
			count += 1
		else:
			if count > 1:
				s += str(count)
				count = 1
			s += current
	if count > 1:
		s += str(count)
	return s


st = "wwwwaaadexxxxxx"
print(compression1(st))
print(compression2(st))
