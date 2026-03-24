"""we want to find the sum of values in array using recursion
say [1,2,3,4] which is 10 so for every element i in the array we want to 
add it to the next value beside it which means we would do i+1
 and we want the loop to stop when there is nothing in the array anymore
 so the code implementation is below"""

def sum_array(arr,i=0):
    if i == len(arr):
        return 0
    return arr[i] + sum_array(arr, i+1)

arr = [1,2,3,4,5,6,7,8,9]

print(sum_array(arr,i=0))
 
