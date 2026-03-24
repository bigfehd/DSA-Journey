"""In this code we are trying to sort the numbers in a particular array
so we would have the start and the end of our sub array"""
def insertion_sort_subarray(arr, start, end):
    """so here the range is start+1 because the array 2 to 5 is [14,5,16,17]
    so we leave index 0 because we assume it sorted, so we loop from 5 to 17
    that is why the range is start + 1 because we start from 5 and the end + 1
    because we need to make sure the range covers 17 because of indexing rule...
    this is a bounded problem...
     """
    for i in range(start+1,end+1):
        """so the key is the first index in the range we are trying to sort
        and j is what we are comparing the key against, so j is outisde the range
        that is why j=i-1....
        so the condition is as far as j>=0 and arr[j] > key; 
        arr[j+1] = arr[j] we shift j to the right
        then we have to check the left again if there are any numbers greater than key
        thats why we do j-=1.....
        
        arr[j+1] = key
        """
    
        key = arr[i]
        j = i-1
        while j>=start and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = key
    
    return arr

arr = [12, 3, 14, 5, 16, 17, 8]
start = 2
end = 5

print(insertion_sort_subarray(arr, start, end)) 
    