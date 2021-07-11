# Pair Star
# Send Feedback
# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
# Input format :
# String S
# Output format :
# Modified string
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a
def check(s,i, str=""):
    if len(s)-1==i:
        str=str+s[i]
        return str
    else:
        if s[i]==s[i+1]:
            str=str+s[i]+"*"
        else:
            str=str+s[i]
        return check(s,i+1, str)
s=input()
print(check(s,0))

def polestar(s):
    if len(s)<=1:
        return s
    if s[0]!=s[1]:
        return s[0]+polestar(s[1:])
    else:
        return s[0]+"*"+polestar(s[1:])
            

