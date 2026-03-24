"""THIS CODE IS FOR SORTING THE NUMBERS IN AN ARRAY
"""



def insertion_sort(arr):
    """so first thing we gotta do is loop through our array, but we assume 
    the first index is sorted which is 0, so our range will be from the second
    index which is at 1 
    """
    
    for i in range(1, len(arr)):
        """what i wanna do next is define a key that i would compare with the inital index not in our i
        so i is the array we wanna work with so key is the first index of that array
        but the first number in the main array is not part of i but before i
        so we can call that first number j, and it is safe to say j = i-1
        """
        key = arr[i]
        j = i-1
        """we have defined the constraints we want to work with,
        so now we do the comparison next. in the comparison
        the conditon is that j must always be greater than or = 0
         and j must be greater than k thats when we can shift, so arr[j] > key"""
         
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            
            """so now we do j-=1, because for every shift we do we are moving j to the left.
            so everytime we move j to the left we have a new j and the current j becomes j+1 which is
            which is where we insert key one step to the right of j"""
            j-=1
            
        arr[j+1] = key
    
    return arr

arr = [7,4,8,9,1,2]

print(insertion_sort(arr))