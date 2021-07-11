# Geometric Sum
# Send Feedback
# Given k, find the geometric sum i.e.
# 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 
# using recursion.
# Input format :
# Integer k
# Output format :
# Geometric sum (upto 5 decimal places)
# Constraints :
# 0 <= k <= 1000
# Sample Input 1 :
# 3
# Sample Output 1 :
# 1.87500
# Sample Input 2 :
# 4
# Sample Output 2 :
# 1.93750

def sum(k):
    if k<1:
        x = k + sum(k*2)
        return x
    else:
        return 1
i=int(input())
print ('%.5f' % sum(float(1/(2**i))))