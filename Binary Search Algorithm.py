"""
Code by DanialHMD
"""

def binary(k , arr , great , small):
    
    if great>=small:

        mid=(great+small)//2
        
        if arr[mid]==k:
            return mid #Returning the position of the key which is the middle
        
        elif arr[mid] > k:
            return binary(k , arr , mid-1 , 0) #Running the function again but the highest value in array is the middle
        
        else:
            return binary(k , arr , great , mid+1) #Running the function again but the lowest value in array is the middle
        
    else:
        return -1 #return if value doesn't exist in the array
        
array=[1,5,24,10,13,9,20,34,2,3] #Array with values
key=9 #key value that we are looking for
array.sort() #in case if array isn't sorted

result=binary(key, array, len(array)-1, 0) #calling function and saving the return values

#showing the result to user
if result != -1:
    print("Value found in index: ", str(result))
    print(array)
else:
    print("Value isn't in the array.")