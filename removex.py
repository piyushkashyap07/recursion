# Remove X
# Send Feedback
# Given a string, compute recursively a new string where all 'x' chars have been removed.
# Input format :
# String S
# Output format :
# Modified String
# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string S. 
# Sample Input 1 :
# xaxb
# Sample Output 1:
# ab
# Sample Input 2 :
# abc
# Sample Output 2:
# abc
# Sample Input 3 :
# xx
# Sample Output 3:


def remove_x(s,x="x"):
    if(len(s)==0):
        return s
    smalloutput=remove_x(s[1:],x)
    if(s[0]==x):
        return smalloutput
    else:
        return s[0]+smalloutput
a=remove_x(input())
print(a)