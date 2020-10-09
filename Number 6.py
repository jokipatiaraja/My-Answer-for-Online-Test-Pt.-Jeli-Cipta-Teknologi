
def solutionNumberSix(n):
    if n<=0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return solutionNumberSix(n-1)+solutionNumberSix(n-2)
        
print(solutionNumberSix(9))