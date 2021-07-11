# Multiplication (Recursive)
# Send Feedback
# Given two integers M & N, calculate and return their multiplication using recursion. You can only use subtraction and addition for your calculation. No other operators are allowed.
# Input format :
# Line 1 : Integer M
# Line 2 : Integer N
# Output format :
# M x N
# Constraints :
# 0 <= M <= 1000
# 0 <= N <= 1000
# Sample Input 1 :
# 3 
# 5
# Sample Output 1 :
# 15
# Sample Input 2 :
# 4 
# 0
# Sample Output 2 :
# 0

from sys import setrecursionlimit
setrecursionlimit(10**6) 

def fun(m,n):
    if n==0:
        return 0
    return m+fun(m,n-1)

m =int(input())
n = int(input())
print(fun(m, n))

def multiplyfunhelp(m,n):
    if m==0 or n==0:
        return 0
    if n>0:
        smallans=multiplyfun(m,n-1)
        return smallans +m
    else:
        smallans=multiplyfun(m,n+1)
        return smallans-m
multiplyfunhelp(0,7)