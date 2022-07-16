def compression1(st):
	temp = []
	comp2 = ""
	for i in range(0,len(st)):
		for j in range(1, len(st)):
			if st[i] == st[j]:
				print("")
			else:
				temp.append(st[i])

	return print(temp)




st = "wwwwaaadexxxxxx"
compression1(st)
