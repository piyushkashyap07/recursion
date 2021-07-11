# Quick Sort Code
# Send Feedback
# Sort an array A using Quick Sort.
# Change in the input array itself. So no need to return or print anything.


# Input format :
# Line 1 : Integer n i.e. Array size
# Line 2 : Array elements (separated by space)
# Output format :
# Array elements in increasing order (separated by space)
# Constraints :
# 1 <= n <= 10^3
# Sample Input 1 :
# 6 
# 2 6 8 5 4 3
# Sample Output 1 :
# 2 3 4 5 6 8
# Sample Input 2 :
# 5
# 1 5 2 7 3
# Sample Output 2 :
# 1 2 3 5 7 

def quickSort(arr, si, ei):
    if si>=ei:
        return
    pivot_index=partition(a,si,ei)
    quickSort(a,si,pivot_index-1)
    quickSort(a,pivot_index+1,ei)
def partition(a,si,ei):
    pivot=a[si]
    c=0
    for i in range(si,ei+1):
        if a[i]<pivot:
            c+=1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index=si+c
    i=si
    j=ei
    
    while i<j:
        if a[i]<pivot:
            i+=1
        elif a[j]>=pivot:
            j-=1
        else:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    return pivot_index

n=int(input())
a=list(int(i) for i in input().strip().split(' '))
quickSort(a, 0, len(a)-1)
print(*a)
