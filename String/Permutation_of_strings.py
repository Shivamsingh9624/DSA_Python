def solution(s):
	sub = []
	for i in range(len(s)):
		for j in range(i + 1, len(s) + 1):
			sub.append(s[i:j])
	return sub

s = "abc"
print(solution(s))