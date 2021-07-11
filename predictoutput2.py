What will be the output of this code?
def printNumbers(n):
    if(n<0):
        return
    print(n,end=" ")
    printNumbers(n-2)
num = 5
printNumbers(num)


Options
Recursion Error
5 4 3 2 1
5 3 1 
None of the above



Correct Answer: 531