n = int(input())
k = int(input())

temp = n
count = 0
while temp > 0:
	temp = temp // 10
	count = count + 1

k = k % count
if k < 0:
	k = k + count

div = 1
mul = 1
for i in range(1, count+1):
	if i <= k:
		div = div * 10
	else:
		mul = mul * 10
q = n / div
r = n % div

rot = int(r * mul + q)
print(rot)
