# Binary-Search
One of the famous, useful methods used for finding a value in sorted list of values.
Binary search, AKA half interval search, AKA logarithmic search, is a method to find the position of a specific value in a sorted array.
### How does it work?
For the beginning, algorithm will compare key value with the middle of the array, if they match, it will return the position and exit; but if it didn't match and it was greater than the middle value, it will comtinue the process on the upper half, in opposite if it was smaller than middle, the process will continue in lower half. it will keep repeating until it finds the match and it will return the position in the array.
### Example Code
Ok so basically for example we have an array like:
```
array=[1,5,24,10,13,9,20,34,2,3]
```
>this array isn't sorted right now so make sure you sort it **before** using it.

and we are trying to find a specific value's position in the array like `key = 9`.

Now we have to write a function called `binary` for searching method:
```
def binary(k , arr , great , small):
    
    if great>=small:

        mid=(great+small)//2
        
        if arr[mid]==k:
            return mid 
        
        elif arr[mid] > k:
            return binary(k , arr , mid-1 , 0) 
        
        else:
            return binary(k , arr , great , mid+1) 
        
    else:
        return -1 #return if value doesn't exist in the array
```
basically these function gets 4 values:
* key value
* array
* great which is the last index of array
* small which in start is 0

you can write this function with recursive or without it, both ways work.

The way it works is that we put an `if` statement in the beginning to check if the array has any index left to compare or not, if yes then it will calculate the middle of array and compare it with `key` value, there will be three other statement:
1. key and middle values are equal
2. key value is greater than middle value
3. middle value is greater than key value

on statement 1 it will return the index of the value and will exit the terminal. On statements 2 & 3 if the condition is true in order it will recall the function with new great or small values which will be middle value we got in the start of `if` statemant:
* for arr[mid]>k: `return binary(k , arr , mid-1 , 0)`
* for arr[mid]<k: `return binary(k , arr , great , mid+1)`

this will continue until the middle value is equal to key value.

If the condition isn't true and there's no more index left in array to compare it will return `-1` value to tell that the value isn't in the array you are looking for.

There are some notes that you have to observe:
* array **MUST** be **Sorted**.
* key value type **MUST** match the value types in array.
* Don't forget to call the function when you want to run the code ;)
