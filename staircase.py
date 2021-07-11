# Staircase
# Send Feedback
# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
# Input format :
# Integer N
# Output Format :
# Integer W
# Constraints :
# 1 <= N <= 30
# Sample Input 1 :
# 4
# Sample Output 1 :
# 7
# Sample Input 2 :
# 5
# Sample Output 2 :
# 13


def return_no_of_ways(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        x=return_no_of_ways(n-3)
        y=return_no_of_ways(n-2)
        z=return_no_of_ways(n-1)
        return x+y+z

n=int(input())
ans=return_no_of_ways(n)
print(ans)

