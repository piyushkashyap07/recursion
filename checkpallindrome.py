# Check Palindrome (recursive)
# Send Feedback
# Check whether a given String S is a palindrome using recursion. Return true or false.
# Input Format :
# String S
# Output Format :
# 'true' or 'false'
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# racecar
# Sample Output 1:
# true
# Sample Input 2 :
# ninja
# Sample Output 2:
# false
def pallindromecheck(s):
    n=len(s)
    if n<=1:
        return True
    if s[0]!=s[n-1]:
        return False
    return pallindromecheck(s[1:-1])
S=input()
pallindromecheck(s)
    