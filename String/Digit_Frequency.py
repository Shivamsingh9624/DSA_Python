# 1. Each digit (0 to 9) denotes the student of the Optica Student community.
#
# 2. You are given a number n where ith digit denotes that ith task that is assigned to the corresponding digit student.
#
# 2. You are given a digit d denotes a student.
#
# 3. You are required to calculate the frequency of digit d in number n or how many tasks are assigned to student d.
#

# Sample Input
#
# 994543234
#  4
#
# Sample Output
# 3

def freq(n, d):
    count = 0
    while n > 0:
        dig = n % 10
        n = n // 10
        if dig == d:
            count += 1
    return count


n = int(input())
d = int(input())
print(freq(n, d))
