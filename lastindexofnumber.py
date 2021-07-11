# Last Index Of Number Question
# Send Feedback
# Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
# Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
# You should start traversing your array from 0, not from (N - 1).
# Do this recursively. Indexing in the array starts from 0.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x
# Output Format :
# last index or -1
# Constraints :
# 1 <= N <= 10^3
# Sample Input :
# 4
# 9 8 10 8
# 8
# Sample Output :
# 3
def lastindex(arr,x,si):
    N=len(arr)
    if si==N:
        return -1
    output=lastindex(arr,x,si+1)
    if output!=-1:
        return output
    else:
        if arr[si]==x:
            return si
        else:
            return -1

N=int(input())
arr=[int(n) for n in input().split()]
x=int(input())
print(lastindex(arr,x,0))