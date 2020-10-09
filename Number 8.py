def solutionNumberEight(arr): 
    length = len(arr) 
    arr.sort() 
    print("Largest element is:", arr[length-1]) 
    print("Smallest element is:", arr[0]) 

arr = [9,12,3,100,4,10,115]

solutionNumberEight(arr)