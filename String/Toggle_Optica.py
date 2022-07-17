# Example

# Sample Input
# pepCODinG
#
# Sample Output
# PEPcodINg

def toggle(st):
	temp = ""
	for i in st:
		if i >= 'a' and i <= 'z':
			temp += i.upper()
		else:
			temp += i.lower()
	return temp


st = "pepCODinG"
print(toggle(st))
