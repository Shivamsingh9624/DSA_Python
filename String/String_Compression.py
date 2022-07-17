# 1. You are given a string.
# 2. You have to compress the given string in the following two ways -
#    First compression -> The string should be compressed such that consecutive duplicates of characters are replaced with a single character.
#    For "aaabbccdee", the compressed string will be "abcde".
#    Second compression -> The string should be compressed such that consecutive duplicates of characters are replaced with the character and followed by the number of consecutive duplicates.
#    For "aaabbccdee", the compressed string will be "a3b2c2de2".

# Sample Input
# wwwwaaadexxxxxx

# Sample Output
# wadex
# w4a3dex6


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
