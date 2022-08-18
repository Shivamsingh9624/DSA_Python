def majority_elements(arr):
	count = 0
	ans = 0

	for i in arr:
		if count == 0:
			ans = i
			count += 1
			continue
		if i == ans:
			count += 1
		else:
			count -= 1

	# verify = 0
	# for j in arr:
	# 	if j == ans:
	# 		verify += 1
	# print(verify, " times the element is found")
	return ans


arr = [1, 1, 2, 3, 1, 2, 1, 1, 2, 2]
print("frequently occurrence element is: ", majority_elements(arr))