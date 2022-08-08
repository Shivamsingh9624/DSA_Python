# Format
# Input
# A number n
# n1
# n2
# .. n number of elements
#
# Output
# A bar chart of asteriks representing value of array a
#
# Example
# Sample Input
#
# 5
# 3
# 1
# 0
# 7
# 5
#
# Sample Output
# 			*
# 			*
# 			*	*
# 			*	*
# *			*	*
# *			*	*
# *	*		*	*

# This is not proper code
def bar_chart(arr,n):
    maximum = max(arr)
    for i in range(maximum, -1, -1):
        # print("i is" ,i)
        for j in range(0, n):
            # print("j is" ,j)
            if arr[j] >= i:
                print("*\t")
            else:
                print("\t")
        print(end = "\n")

#write your code here
n=int(input())
arr = []
for i in range(n):
    temp = int(input())
    arr.append(temp)
bar_chart(arr,n)