def solutionNumberSeven(myString):
     
    # If at any time we encounter 2 
    # same characters, return false
    for i in range(len(myString)):
        for j in range(i + 1,len(myString)): 
            if(myString[i] == myString[j]):
                return False;
 
    # If no duplicate characters 
    # encountered, return true
    return True;
        
if(solutionNumberSeven("sfrere")):
    print("The String ", str," has all unique characters");
else:
    print("The String ", str, " has duplicate characters");